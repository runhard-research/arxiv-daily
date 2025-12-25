import sys
import yaml
import requests
import re
from datetime import datetime
from xml.etree import ElementTree as ET

SEEN_ARXIV_IDS = set()
ARXIV_API = "http://export.arxiv.org/api/query"

def extract_arxiv_id(link: str):
    """
    http://arxiv.org/abs/2512.19673v1
    → 2512.19673
    """
    m = re.search(r'arxiv\.org/abs/([0-9]+\.[0-9]+)', link)
    return m.group(1) if m else None


def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def fetch_arxiv(categories, max_results):
    query = " OR ".join([f"cat:{c}" for c in categories])

    params = {
        "search_query": query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": max_results,
    }

    r = requests.get(ARXIV_API, params=params, timeout=30)
    r.raise_for_status()
    return r.text

def summarize_abstract_first_n(abstract: str, n: int = 2):
    """
    Extract first n sentences from abstract.
    """
    if not abstract:
        return []

    text = abstract.replace("\n", " ").strip()
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return sentences[:n]


def parse_entries(xml_text):
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_text)
    entries = []

    for e in root.findall("a:entry", ns):
        title = e.find("a:title", ns).text.strip().replace("\n", " ")
        summary = e.find("a:summary", ns).text.strip().replace("\n", " ")
        published = e.find("a:published", ns).text
        link = e.find("a:id", ns).text

        entries.append({
            "title": title,
            "summary": summary,
            "text": f"{title} {summary}".lower(),
            "year": int(published[:4]),
            "link": link,
        })
    return entries


def apply_filter(entries, flt):
    result = []
    for e in entries:
        text = e["text"]

        if flt.get("min_year") and e["year"] < flt["min_year"]:
            continue

        if flt.get("exclude"):
            if any(w.lower() in text for w in flt["exclude"]):
                continue

        if flt.get("must"):
            if not all(w.lower() in text for w in flt["must"]):
                continue

        if flt.get("keywords"):
            if not any(w.lower() in text for w in flt["keywords"]):
                continue

        result.append(e)

    return result

def deduplicate_by_first_seen(entries):
    deduped = []

    for e in entries:
        arxiv_id = extract_arxiv_id(e["link"])
        if not arxiv_id:
            continue

        if arxiv_id in SEEN_ARXIV_IDS:
            continue  # すでに別分野で採用済み

        SEEN_ARXIV_IDS.add(arxiv_id)
        deduped.append(e)

    return deduped


def build_markdown(entries):
    lines = []
    for e in entries:
        summary_lines = summarize_abstract_first_n(e["summary"], n=2)

        lines.append(f"### {e['title']}")
        lines.append(f"- **arXiv**: {e['link']}")
        lines.append(f"- **Summary**:")

        for s in summary_lines:
            lines.append(f"  - {s}")

        lines.append("")  # 空行

    return "\n".join(lines) if lines else "_No papers found._"


def update_readme(tag, md_block):
    with open("README.md", "r") as f:
        content = f.read()

    start = f"<!-- START:{tag} -->"
    end = f"<!-- END:{tag} -->"

    new = f"{start}\n{md_block}\n{end}"

    content = re.sub(
        f"{start}[\\s\\S]*?{end}",
        new,
        content
    )

    today = datetime.now().strftime("%Y-%m-%d")
    content = re.sub(
        r"_Last updated:.*_",
        f"_Last updated: {today}_",
        content
    )

    with open("README.md", "w") as f:
        f.write(content)


def main(cfg_path):
    cfg = load_config(cfg_path)

    query_cfg = cfg["query"]

    if "categories" in query_cfg:
        categories = query_cfg["categories"]
    elif "category" in query_cfg:
        categories = [query_cfg["category"]]
    else:
        raise ValueError("query must have 'category' or 'categories'")

    xml = fetch_arxiv(
        categories,
        query_cfg.get("max_results", 20)
    )

    entries = parse_entries(xml)
    filtered = apply_filter(entries, cfg.get("filter", {}))
    deduped = deduplicate_by_first_seen(filtered)
    md = build_markdown(deduped)

    update_readme(cfg["tag"], md)
    print(f"[OK] Updated section: {cfg['tag']} ({len(filtered)} papers)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fetch_arxiv.py configs/vision.yaml")
        sys.exit(1)

    main(sys.argv[1])

