import feedparser

FEED_URL = "https://dailydarkweb.net/feed"

# Parse RSS feed
feed = feedparser.parse(FEED_URL)

# Ambil 3 item terbaru
items = feed.entries[:3]

# Format RSS XML
rss_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>{feed.feed.title}</title>
  <link>{feed.feed.link}</link>
  <description>{feed.feed.description}</description>
"""

for item in items:
    rss_content += f"""
  <item>
    <title>{item.title}</title>
    <link>{item.link}</link>
    <description>{item.description}</description>
    <pubDate>{item.published}</pubDate>
  </item>
"""

rss_content += """
</channel>
</rss>
"""

# Simpan ke file rss.xml
with open("rss.xml", "w", encoding="utf-8") as f:
    f.write(rss_content)

print("RSS XML file generated successfully.")
