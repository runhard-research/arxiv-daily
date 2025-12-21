import feedparser
import yaml
from datetime import datetime

ARXIV_API = "http://export.arxiv.org/api/query"

def load_config():
    with open("config.yml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def fetch_papers(cfg):
    query = f"cat:{cfg['query']['category']}"
    url = (
        f"{ARXIV_API}"
        f"?search_query={query}"
        f"&sortBy=submittedDate"
        f"&sortOrder=descending"
        f"&max_results={cfg['max_results']}"
    )
    return feedparser.parse(url).entries

def format_md(entries):
    lines = []
    for e in entries:
        title = e.title.replace("\n", " ")
        link = e.link
        date = e.published[:10]
        lines.append(f"- **{title}**  \n  {date} | [arXiv]({link})")
    return "\n\n".join(lines)

def update_readme(content):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(
            "# arXiv Daily Papers\n\n"
            f"_Last update: {datetime.utcnow().isoformat()} UTC_\n\n"
            "## Latest Papers\n\n"
            f"{content}\n"
        )

if __name__ == "__main__":
    cfg = load_config()
    papers = fetch_papers(cfg)
    md = format_md(papers)
    update_readme(md)

