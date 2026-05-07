#!/usr/bin/env python3
"""Genera sitemap.xml en la raíz del proyecto a partir de articles.json + páginas estáticas."""
import json
import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
ARTICLES = ROOT / "blog" / "articles.json"
SITEMAP_OUT = ROOT / "sitemap.xml"
SITE_BASE = "https://credipro.com.mx"

with open(ARTICLES, "r", encoding="utf-8") as f:
    articles = json.load(f)

today = datetime.now().strftime("%Y-%m-%d")

urls = [
    (f"{SITE_BASE}/", today, "1.0", "weekly"),
    (f"{SITE_BASE}/blog/", today, "0.9", "weekly"),
    (f"{SITE_BASE}/nosotros/", today, "0.7", "monthly"),
    (f"{SITE_BASE}/simulador/", today, "0.9", "monthly"),
    (f"{SITE_BASE}/contacto/", today, "0.5", "monthly"),
]

for art in articles:
    slug = art.get("slug")
    if not slug:
        continue
    fecha = art.get("fecha", today)
    urls.append((f"{SITE_BASE}/blog/p/{slug}/", fecha, "0.8", "monthly"))

xml = ['<?xml version="1.0" encoding="UTF-8"?>']
xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
for url, lastmod, priority, changefreq in urls:
    xml.append("  <url>")
    xml.append(f"    <loc>{url}</loc>")
    xml.append(f"    <lastmod>{lastmod}</lastmod>")
    xml.append(f"    <changefreq>{changefreq}</changefreq>")
    xml.append(f"    <priority>{priority}</priority>")
    xml.append("  </url>")
xml.append("</urlset>")

SITEMAP_OUT.write_text("\n".join(xml), encoding="utf-8")
print(f"  Sitemap generado: {SITEMAP_OUT}")
print(f"  URLs incluidas: {len(urls)}")
