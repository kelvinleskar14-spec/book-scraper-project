# 📊 Professional Book Catalogue Web Scraper & Data Extractor

A robust, enterprise-ready Python web scraping solution engineered to extract structured product data (titles, pricing architectures, and real-time stock levels) from online book catalogues and export them directly to business-ready spreadsheets.

This repository serves as a functional showcase of my technical data extraction capabilities for potential business clients, e-commerce managers, and data analysts.

---

## 💼 Need Custom Scraping or Data Automation Services?
I specialize in building custom, high-performance data extraction pipelines tailored to your business needs. Whether you need to monitor competitor pricing, aggregate real-time market data, or feed structured data into AI/ML models, I can build it for you.

* **Developer:** Kelvin Leskar
* **Specialization:** AI & Machine Learning | Data Automation Engineering
* **Inquiries:** [kelvinleskar14@gmail.com](mailto:kelvinleskar14@gmail.com)
* **Availability:** Open for freelance projects, contract roles, and custom script development.

---

## ⚡ Key Capabilities & Client Value
* **Automated Excel Exporting:** Automatically cleans raw web information and formats it into organized Excel (`.xlsx`) spreadsheets for non-technical users.
* **Precision Extraction:** Isolates and extracts granular data fields including exact book titles, numeric prices, and inventory stock availability status.
* **Resilient Architecture:** Implements optimized HTTP requests and header rotations to ensure consistent data delivery and bypass basic server-side rate limits.
* **ML-Ready Outputs:** Built with structured data principles, allowing the scraped outputs to be seamlessly cleaned and fed directly into analytics pipelines or Machine Learning models.

---

## 📋 Sample Extracted Data Output (Excel Sample)
When the pipeline executes, it generates a clean Excel workbook containing structured data points like this:

| Book Title | Price | Stock Availability | Extraction Date |
| :--- | :--- | :--- | :--- |
| A Light in the Attic | £51.77 | In Stock (22 available) | 2026-10-24 |
| Tipping the Velvet | £53.74 | In Stock (20 available) | 2026-10-24 |
| Soumission | £50.10 | In Stock (19 available) | 2026-10-24 |
| Sharp Objects | £47.82 | Out of Stock | 2026-10-24 |

---

## 🛠️ Tech Stack & Engineering Concepts Demonstrated
* **Core Language:** Python 3.x
* **Network Communication:** `Requests` (handling synchronous HTTP queries)
* **HTML Parsing Engine:** `BeautifulSoup4` (efficient DOM navigation and CSS selectors)
* **Data Formatting:** `pandas` / `openpyxl` (handling clean data exports to Excel)
* **Robust File Structure:** Configured with clean `.gitignore` patterns to prevent junk or local Excel file leaks from entering production.

---

## 📦 Project Architecture
```text
book-scraper-project/
├── .gitignore          # Production filter excluding virtual environments & local Excel outputs
├── README.md           # Business and technical documentation (You are here!)
├── requirements.txt    # Frozen production dependencies for seamless deployment
└── scraper.py          # The core data extraction and Excel export pipeline script
```

---

## ⚙️ Quick Start for Technical Reviewers

### 1. Clone & Navigate
```bash
git clone https://github.com
cd book-scraper-project
```

### 2. Environment Setup
* **Windows:**
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```
* **macOS/Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Execute Pipeline
```bash
python scraper.py
```
*(Upon a successful run, a newly populated Excel spreadsheet will automatically appear in your folder).*

---

## 🚀 Advanced Services I Can Add For Your Business
If you decide to hire me for a custom project, I can easily expand this architecture to include:
1. **Automated Cloud Schedulers:** Running scrapers on a daily or hourly cron job on AWS/DigitalOcean to keep your databases fresh.
2. **Deep AI Integration:** Passing scraped unstructured web data through Natural Language Processing (NLP) models for sentiment analysis, programmatic summarization, or automatic categorization.
3. **Advanced Anti-Bot Bypassing:** Implementing cloud proxy rotation and dynamic headless browsers (Playwright/Selenium) to scrape heavy JavaScript-rendered sites.

