📚 Advanced Book Scraper Bot (Selenium + Telegram Integration)
🧠 Overview

This is a Python-based automation project that scrapes book data from a website using Selenium, saves it into a CSV file using Pandas, and automatically sends both a notification and the generated file to your Telegram account.

It is designed for learning web scraping, automation, and API integration in a real-world project structure.

⚙️ Tech Stack
Python 3.x
Selenium (Web Automation)
Pandas (Data Handling)
Requests (Telegram API communication)
python-dotenv (Environment Variable management)
webdriver-manager (Automatic ChromeDriver handling)
🚀 Features
🔍 Automated book data scraping (title, price, etc.)
📊 Structured CSV file generation (scraped_books.csv)
📱 Telegram instant notification after completion
📎 Automatic file sending to Telegram chat
🔐 Secure credential handling using .env
⚠️ Basic error handling for scraping and API failures
🧩 Clean and modular Python script structure
📁 Project Structure
book-scraper-bot/
│
├── book_scraper.py
├── .env
├── requirements.txt
├── scraped_books.csv   (generated after run)
└── README.md
🛠️ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/deva-automation/book-scraper-bot.git
cd book-scraper-bot
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install selenium pandas requests python-dotenv webdriver-manager

OR (if you use requirements file):

pip install -r requirements.txt
4️⃣ Create .env File

Create a file named .env in the root folder:

BOT_TOKEN=your_telegram_bot_token_here
CHAT_ID=your_telegram_chat_id_here
🔐 How to get these:
BOT_TOKEN → From Telegram @BotFather
CHAT_ID → From @userinfobot
▶️ How to Run the Project
python book_scraper.py
📂 Output Explanation

After running the script:

📄 CSV File
scraped_books.csv

Contains all scraped book data in structured format.

📱 Telegram Output
Success message sent to your Telegram
CSV file automatically delivered to your chat
🧠 How It Works (Logic Flow)
Selenium opens the target website
Scrapes book data (title, price, availability)
Stores data using Pandas DataFrame
Saves data into CSV file
Sends file + message via Telegram Bot API
📌 Important Notes
Make sure Chrome browser is installed
Keep ChromeDriver compatible (handled automatically by webdriver-manager)
Do NOT share your .env file publicly
👨‍💻 Author

Deva
Python Automation Developer (Learning & Building Real-world Projects)
