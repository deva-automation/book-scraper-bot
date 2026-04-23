from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("http://books.toscrape.com/")
time.sleep(3)

book_names = []
book_prices = []


books = driver.find_elements(By.CLASS_NAME, "product_pod")

for book in books:
    name = book.find_element(By.TAG_NAME, "h3").text
    book_names.append(name)   
    
    price = book.find_element(By.CLASS_NAME, "price_color").text
    book_prices.append(price)
    
data = {
    "Book name" : book_names,
    "price" : book_prices
}

df = pd.DataFrame(data)

df.to_csv("my_books_data.csv", index=False)

driver.quit()

print("✅ Data saved successfully!")
