#!/usr/bin/env python
"""Toolora Sitemap Generator"""

from datetime import datetime

def generate_sitemap():
    """Generate sitemap.xml for SEO"""
    sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml"
        xmlns:mobile="http://www.google.com/schemas/sitemap-mobile/1.0"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
        xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">

    <!-- Main Pages -->
    <url>
        <loc>https://toolora.com/</loc>
        <lastmod>''' + datetime.now().strftime('%Y-%m-%d') + '''</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
        <xhtml:link rel="alternate" hreflang="fa" href="https://toolora.com/?lang=fa"/>
        <xhtml:link rel="alternate" hreflang="de" href="https://toolora.com/?lang=de"/>
        <xhtml:link rel="alternate" hreflang="he" href="https://toolora.com/?lang=he"/>
        <xhtml:link rel="alternate" hreflang="en" href="https://toolora.com/?lang=en"/>
    </url>

    <url>
        <loc>https://toolora.com/about</loc>
        <lastmod>''' + datetime.now().strftime('%Y-%m-%d') + '''</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>

    <url>
        <loc>https://toolora.com/privacy</loc>
        <lastmod>''' + datetime.now().strftime('%Y-%m-%d') + '''</lastmod>
        <changefreq>yearly</changefreq>
        <priority>0.5</priority>
    </url>

    <url>
        <loc>https://toolora.com/terms</loc>
        <lastmod>''' + datetime.now().strftime('%Y-%m-%d') + '''</lastmod>
        <changefreq>yearly</changefreq>
        <priority>0.5</priority>
    </url>

    <!-- Tools -->
    <url>
        <loc>https://toolora.com/word-counter</loc>
        <lastmod>''' + datetime.now().strftime('%Y-%m-%d') + '''</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>

    <url>
        <loc>https://toolora.com/character-counter</loc>
        <lastmod>''' + datetime.now().strftime('%Y-%m-%d') + '''</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>

    <url>
        <loc>https://toolora.com/text-cleaner</loc>
        <lastmod>''' + datetime.now().strftime('%Y-%m-%d') + '''</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>

    <url>
        <loc>https://toolora.com/json-formatter</loc>
        <lastmod>''' + datetime.now().strftime('%Y-%m-%d') + '''</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>

</urlset>'''
    return sitemap

if __name__ == "__main__":
    print(generate_sitemap())
