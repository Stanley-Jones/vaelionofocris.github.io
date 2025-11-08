#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import argparse

def build_sitemap(root: Path, site_root: str) -> str:
    # Collect HTML pages (root + subdirs). Exclude drafts, temp, and common non-indexable pages.
    exclude_names = {"404.html", "cancel.html", "success.html"}
    exclude_subdirs = {".git", ".github", "node_modules", "_drafts", "_private"}

    html_files = []
    for p in root.rglob("*.html"):
        # Exclude hidden and excluded dirs
        if any(part in exclude_subdirs for part in p.parts):
            continue
        if p.name in exclude_names:
            continue
        # Skip generated alternates like *_with_books_excerpts.html
        if "with_books_excerpts" in p.name:
            continue
        html_files.append(p)

    # Ranking heuristics
    def page_meta(p: Path):
        name = p.name
        if name == "index.html":
            return "weekly", "1.0"
        elif name in {"about.html", "manifesto.html", "blog.html", "books-excerpts.html"}:
            return "weekly", "0.8"
        elif "/posts/" in p.as_posix():
            return "weekly", "0.6"
        else:
            return "monthly", "0.5"

    def to_url(p: Path) -> str:
        rel = p.relative_to(root).as_posix()
        return f"{site_root}/{rel}"

    entries = []
    for f in sorted(html_files):
        changefreq, priority = page_meta(f)
        try:
            lastmod = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc).date().isoformat()
        except Exception:
            lastmod = datetime.now(timezone.utc).date().isoformat()
        entries.append((to_url(f), lastmod, changefreq, priority))

    # Compose XML
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, lastmod, changefreq, priority in entries:
        lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{lastmod}</lastmod>",
            f"    <changefreq>{changefreq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>"
        ]
    lines.append("</urlset>")
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Site root directory")
    ap.add_argument("--site-root", required=True, help="Canonical origin, e.g. https://vaelionofocris.com")
    ap.add_argument("--outfile", default="sitemap.xml", help="Path to write sitemap.xml")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    xml = build_sitemap(root, args.site_root)
    Path(args.outfile).write_text(xml, encoding="utf-8")
    print(f"Wrote {args.outfile}")

if __name__ == "__main__":
    main()
