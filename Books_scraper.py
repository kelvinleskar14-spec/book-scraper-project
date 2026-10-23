import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"}
Base_url = "https://books.toscrape.com/catalogue/"
books_content = []
pages_to_scrape = 50

for x in range (1, pages_to_scrape+1):
    url = f"https://books.toscrape.com/catalogue/page-{x}.html"
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')
        
        if not books:
            print(f"⚠️ Warning: No books found on page {x}. Skipping.")
            continue
        
        for book in books:
            title_link = book.h3.find('a') if book.h3 else None
            if title_link and title_link.has_attr('title'):
                title = title_link['title']
                instant_href = title_link['href']
                book_link= (f"https://books.toscrape.com/catalogue/+{instant_href}")
            else:
                title = "Unknown Title"
                book_link= "Unknown Link"
            price_element = book.find('p', class_='price_color')
            price = price_element.text.strip() if price_element else "N/A"
            availability_element = book.find('p', class_='instock availability')
            availability = availability_element.text.strip() if availability_element else "N/A"
                
        
            books_content.append({'Title': title,
                                    'Price': price,
                                    'availability': availability,
                                    'book_link': book_link})

    except requests.exceptions.RequestException as e:
        print(f"❌ Network error on page {x}: {e}. Continuing to next page...")

    except Exception as e:
        print(f"❌ Parsing error on page {x}: {e}. Continuing to next page...")


    time.sleep(1)

if books_content:
    df =pd.DataFrame(books_content)
    print("\n📊 First 10 Scraped Results:")
    print(df.head(10))

    df.to_excel('scraped_books.xlsx', index=False)
    print("successfully scraped books and saved as scraped_books.xlsx")
else:
    print("\n❌ No data was successfully collected.")