# 📚 Advanced Book Scraper Bot (with Telegram Integration)

## 🧠 Description
This is a professional Python automation script that uses **Selenium** to scrape book data from a website. It not only saves the data into a CSV file but also sends a real-time notification and the generated file directly to your **Telegram** account.

## ⚙️ Technologies Used
- **Python**: Core programming language.
- **Selenium**: Web automation and scraping.
- **Pandas**: Data manipulation and CSV creation.
- **Requests**: Sending data to Telegram API.
- **Dotenv**: Managing secure credentials (.env).

## 🚀 Key Features
- **Automated Scraping**: Extracts book names and prices accurately.
- **Telegram Notifications**: Sends a success message to your phone upon completion.
- **Direct File Delivery**: Automatically sends the `scraped_books.csv` file to your Telegram chat.
- **Secure Credentials**: Keeps your Bot Token and Chat ID safe using Environment Variables.
- **Error Handling**: Built-in logic to handle website loading issues or API errors.

## 🛠️ Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/deva-automation/book-scraper-bot.git](https://github.com/deva-automation/book-scraper-bot.git)
   cd book-scraper-bot
Install required libraries:

Bash
pip install selenium pandas webdriver-manager requests python-dotenv
Configure Secrets:
Create a .env file in the project folder and add your Telegram details:

Plaintext
BOT_TOKEN=your_bot_token_here
CHAT_ID=your_chat_id_here
▶️ How to Run
Simply execute the script:

Bash
python book_scraper.py
📂 Output
scraped_books.csv: Local file containing scraped data.

Telegram Alert: Instant message and file delivery on your mobile/desktop.

👨‍💻 Author
Deva (Aspiring Python Automation Developer)
