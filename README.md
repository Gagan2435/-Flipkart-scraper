# 🛒 Flipkart Product Scraper

A Python-based web scraper that extracts **product names, prices, ratings, and reviews** from Flipkart search results and exports the data to a clean CSV file.

---

## 📸 What It Does

- Searches any product on Flipkart (mobiles, laptops, shoes, etc.)
- Scrapes multiple pages automatically
- Extracts: Product Name, Price, Rating, Reviews, Product URL
- Saves everything to a neat **CSV file** in the `output/` folder

---

## 🗂️ Project Structure

```
flipkart-scraper/
│
├── src/
│   └── scraper.py          # Main scraper script
│
├── output/                 # Scraped CSV files saved here
│
├── requirements.txt        # Python dependencies
└── README.md               # You're reading this!
```

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/flipkart-scraper.git
cd flipkart-scraper
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

**1. Open `src/scraper.py` and set your search query:**
```python
SEARCH_QUERY = "laptop"   # Change this to any product
PAGES = 3                  # Number of pages to scrape
```

**2. Run the scraper:**
```bash
python src/scraper.py
```

**3. Find your data in the `output/` folder:**
```
output/flipkart_laptop_20260304_143022.csv
```

---

## 📊 Sample Output

| Product Name | Price | Rating | Reviews | URL |
|---|---|---|---|---|
| HP Laptop 15s | ₹45,990 | 4.3 | (2,341) | flipkart.com/... |
| Lenovo IdeaPad | ₹38,999 | 4.1 | (1,876) | flipkart.com/... |
| Dell Inspiron | ₹52,490 | 4.4 | (987) | flipkart.com/... |

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Requests** — HTTP requests
- **BeautifulSoup4** — HTML parsing
- **Pandas** — Data handling & CSV export

---

## ⚠️ Disclaimer

This project is built for **educational purposes only**. Please respect Flipkart's `robots.txt` and terms of service. Do not use for commercial data harvesting.

---

## 👨‍💻 Author

Made by Gagandeep
BTech Student | Python Developer  
ggagandeep_be23@thapar.edu
