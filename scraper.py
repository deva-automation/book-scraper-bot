import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Load environment variables from .env file
load_dotenv()
TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
TARGET_URL = "http://books.toscrape.com/"

# ---------------------------------------------------------
# FUNCTION SECTION
# ---------------------------------------------------------

def send_telegram_message(message):
    """Send text message to Telegram (GET Request)"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        response = requests.get(url)

        if response.status_code == 200:
            print("✅ Telegram notification sent successfully!")
        else:
            print("❌ Failed to send message.")

    except Exception as e:
        print(f"⚠️ Message error: {e}")


def send_telegram_document(file_path):
    """Send file (CSV/PDF/Image) to Telegram (POST Request)"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"

        with open(file_path, 'rb') as file:
            files = {'document': file}
            data = {'chat_id': CHAT_ID}

            print(f"📂 Sending file '{file_path}' to Telegram...")

            response = requests.post(url, files=files, data=data)

        if response.status_code == 200:
            print("✅ File has been successfully delivered to your Telegram!")
        else:
            print("❌ Failed to send file.")

    except Exception as e:
        print(f"⚠️ File error: {e}")


def scrape_books_data():
    """Scrape book names and prices, then save to CSV"""
    print("🚀 Bot started... Opening browser!")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(TARGET_URL)
        time.sleep(3)

        book_names = []
        book_prices = []

        books = driver.find_elements(By.CLASS_NAME, "product_pod")

        for book in books:
            name = book.find_element(By.TAG_NAME, "h3").text
            price = book.find_element(By.CLASS_NAME, "price_color").text
            book_names.append(name)
            book_prices.append(price)

        data = {
            "Book Name": book_names,
            "Price": book_prices
        }

        df = pd.DataFrame(data)
        file_name = "scraped_books.csv"
        df.to_csv(file_name, index=False)

        print(f"📊 Scraping completed! {len(book_names)} books collected.")

        return len(book_names), file_name

    except Exception as e:
        print(f"⚠️ Error during scraping: {e}")
        return 0, None

    finally:
        driver.quit()
        print("🛑 Browser has been closed.")


# ---------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------
if __name__ == "__main__":

    total_books, saved_file = scrape_books_data()

    if total_books > 0:
        success_msg = f"✅ Scraping completed successfully!\n📚 Total books: {total_books}"
        send_telegram_message(success_msg)

        send_telegram_document(saved_file)

    else:
        send_telegram_message("❌ Scraping failed. Please check the script.")
        