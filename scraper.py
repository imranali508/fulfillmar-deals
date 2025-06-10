# scraper.py

import feedparser

FEED_URL = "https://slickdeals.net/newsearch.php?rss=1&q=clearance"

def scrape_rss_deals(limit=5):
    """
    Pulls the top `limit` clearance deals from Slickdeals RSS.
    """
    feed = feedparser.parse(FEED_URL)
    items = feed.get("entries", [])[:limit]
    deals = []
    for item in items:
        deals.append({
            "title": item.get("title", "No title"),
            "url":   item.get("link"),
            "price": item.get("description", "").split("<")[0].strip()  # plain-text snippet
        })
    return deals

def scrape_all():
    return scrape_rss_deals()

if __name__ == "__main__":
    deals = scrape_all()
    for d in deals:
        print(d)
