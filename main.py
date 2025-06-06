import yfinance as yf
import time
from telegram import Bot
from datetime import datetime
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(token=TELEGRAM_TOKEN)

stocks = ['1120.SR', '2010.SR', '7010.SR']

def send_alert(stock, signal, price):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"📈 تنبيه تداول جديد\n📊 السهم: {stock}\n💡 الإشارة: {signal}\n💰 السعر الحالي: {price:.2f} ريال\n⏰ الوقت: {now}"
    bot.send_message(chat_id=CHAT_ID, text=message)

while True:
    for stock in stocks:
        data = yf.download(stock, period='1d', interval='1m')
        if data.empty:
            continue
        price = data['Close'].iloc[-1]
        if price < 100:  # شرط بسيط كمثال
            send_alert(stock, 'شراء', price)
    time.sleep(60)
