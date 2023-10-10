import smtplib
import time
from forex_python.converter import CurrencyRates

SMTP_SERVER = 'your_smtp_server.com'
SMTP_PORT = 587
YOUR_EMAIL = 'your_email@gmail.com'
YOUR_EMAIL_PASSWORD = 'your_email_password'
RECIPIENT_EMAIL = 'recipient_email@example.com'

BASE_CURRENCY = 'USD'
TARGET_CURRENCY = 'EUR'

ALERT_THRESHOLD = 0.9

def send_email(subject, message):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(YOUR_EMAIL, YOUR_EMAIL_PASSWORD)
        body = f"Subject: {subject}\n\n{message}"
        server.sendmail(YOUR_EMAIL, RECIPIENT_EMAIL, body)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {str(e)}")

def monitor_exchange_rate():
    converter = CurrencyRates()
    while True:
        rate = converter.get_rate(BASE_CURRENCY, TARGET_CURRENCY)
        if rate < ALERT_THRESHOLD:
            subject = f"Currency Alert: {BASE_CURRENCY} to {TARGET_CURRENCY}"
            message = f"Current exchange rate: 1 {BASE_CURRENCY} = {rate} {TARGET_CURRENCY}"
            send_email(subject, message)
        time.sleep(3600)

if __name__ == "__main__":
    monitor_exchange_rate()
