import sys
import yaml
import requests
import re
from datetime import datetime
from xml.etree import ElementTree as ET

ARXIV_API = "http://export.arxiv.org/api/query"


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


def build_markdown(entries):
    lines = []
    for e in entries:
        lines.append(f"- **{e['title']}**  \n  {e['link']}")
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
    md = build_markdown(filtered)

    update_readme(cfg["tag"], md)
    print(f"[OK] Updated section: {cfg['tag']} ({len(filtered)} papers)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fetch_arxiv.py configs/vision.yaml")
        sys.exit(1)

    main(sys.argv[1])

