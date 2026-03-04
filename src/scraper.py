import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import os
from datetime import datetime


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def get_soup(url):
    """Fetch page and return BeautifulSoup object."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not fetch page: {e}")
        return None


def parse_products(soup):
    """Extract product details from search results page."""
    products = []

    # Flipkart product cards
    cards = soup.find_all("div", {"data-id": True})

    for card in cards:
        try:
            # Product name
            name_tag = card.find("div", class_=lambda c: c and "KzDlHZ" in c) or \
                       card.find("a", class_=lambda c: c and "wjcEIp" in c)
            name = name_tag.get_text(strip=True) if name_tag else "N/A"

            # Price
            price_tag = card.find("div", class_=lambda c: c and "Nx9bqj" in c) or \
                        card.find("div", class_=lambda c: c and "_30jeq3" in c)
            price = price_tag.get_text(strip=True) if price_tag else "N/A"

            # Rating
            rating_tag = card.find("div", class_=lambda c: c and "XQDdHH" in c) or \
                         card.find("div", class_=lambda c: c and "_3LWZlK" in c)
            rating = rating_tag.get_text(strip=True) if rating_tag else "N/A"

            # Number of reviews
            reviews_tag = card.find("span", class_=lambda c: c and "Wphh3N" in c) or \
                          card.find("span", class_=lambda c: c and "_2_R_DZ" in c)
            reviews = reviews_tag.get_text(strip=True) if reviews_tag else "N/A"

            # Product URL
            link_tag = card.find("a", href=True)
            link = "https://www.flipkart.com" + link_tag["href"] if link_tag else "N/A"

            if name != "N/A":
                products.append({
                    "Product Name": name,
                    "Price": price,
                    "Rating": rating,
                    "Reviews": reviews,
                    "URL": link,
                })

        except Exception as e:
            print(f"[WARNING] Skipped a product due to error: {e}")
            continue

    return products


def scrape_flipkart(search_query, pages=3):
    """
    Scrape Flipkart search results for a given query.

    Args:
        search_query (str): Product to search (e.g., 'laptop', 'mobile phone')
        pages (int): Number of pages to scrape (default: 3)

    Returns:
        pd.DataFrame: DataFrame with all scraped products
    """
    all_products = []
    query_formatted = search_query.replace(" ", "+")

    print(f"\n{'='*50}")
    print(f"  Flipkart Scraper — Searching: '{search_query}'")
    print(f"  Pages to scrape: {pages}")
    print(f"{'='*50}\n")

    for page in range(1, pages + 1):
        url = f"https://www.flipkart.com/search?q={query_formatted}&page={page}"
        print(f"[INFO] Scraping page {page}: {url}")

        soup = get_soup(url)
        if not soup:
            print(f"[WARNING] Skipping page {page}")
            continue

        products = parse_products(soup)
        all_products.extend(products)
        print(f"[INFO] Found {len(products)} products on page {page}")

        # Polite delay between requests (avoid getting blocked)
        delay = random.uniform(1.5, 3.0)
        print(f"[INFO] Waiting {delay:.1f}s before next request...")
        time.sleep(delay)

    print(f"\n[SUCCESS] Total products scraped: {len(all_products)}")
    return pd.DataFrame(all_products)


def save_results(df, search_query):
    """Save scraped data to CSV file in output folder."""
    if df.empty:
        print("[WARNING] No data to save.")
        return

    os.makedirs("output", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    query_clean = search_query.replace(" ", "_").lower()
    filename = f"output/flipkart_{query_clean}_{timestamp}.csv"

    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"[SAVED] Data saved to: {filename}")
    return filename


def main():
    # ---- CHANGE THIS to scrape any product ----
    SEARCH_QUERY = "laptop"
    PAGES = 3
    # -------------------------------------------

    df = scrape_flipkart(SEARCH_QUERY, pages=PAGES)

    if not df.empty:
        print("\n--- Sample Results (Top 5) ---")
        print(df.head().to_string(index=False))
        save_results(df, SEARCH_QUERY)
    else:
        print("\n[INFO] No products found. Flipkart may have updated its HTML structure.")
        print("[TIP] Update the CSS class names in parse_products() function.")


if __name__ == "__main__":
    main()
