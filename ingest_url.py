# ingest_url.py
import sys
import re
import requests
from bs4 import BeautifulSoup
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

url = sys.argv[1]

headers = {
    "User-Agent": "Mozilla/5.0",
}

resp = requests.get(url, headers=headers, timeout=20, )
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")

print(resp.text)

title = soup.title.string.strip() if soup.title else "untitled"

# 微信公众号正文通常在这个节点
article = soup.select_one("#js_content")

if article:
    text = article.get_text("\n", strip=True)
else:
    # fallback: 普通网页
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    text = soup.get_text("\n", strip=True)

slug = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "-", title).strip("-")[:80]

today = date.today().isoformat()
out_dir = Path("inbox/raw")
out_dir.mkdir(parents=True, exist_ok=True)

out_file = out_dir / f"{today}-{slug}.md"

out_file.write_text(f"""---
title: "{title}"
source: "{url}"
ingested: "{today}"
status: raw
---

# {title}

Source: {url}

---

{text}
""", encoding="utf-8")

print(f"Saved to {out_file}")