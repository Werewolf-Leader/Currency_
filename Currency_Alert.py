from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
import requests
import smtplib
from email.mime.text import MIMEText

# Create the agent
agent = Agent(name="exchange_rate_agent",
              endpoint=["http://127.0.0.1:8000/submit"],
              seed="your_recovery_phrase_here")

# Function to fetch the exchange rate
def get_rate(base, target):
    response = requests.get(f'https://v6.exchangerate-api.com/v6/86639d518e130c5da8c502d2/latest/{base}')
    data = response.json()
    rates = data.get('conversion_rates', {})
    return rates.get(target)

# Function to check thresholds and send email alerts
def check_thresholds():
    base = "USD"
    target = "INR"
    upper = 82.60
    lower = 82.55
    rate = get_rate(base, target)

    if rate:
        if rate > upper:
            send_notification(f'Alert: {base} to {target} rate is above {upper}')
        elif rate < lower:
            send_notification(f'Alert: {base} to {target} rate is below {lower}')

# Function to send email alerts
def send_notification(message):
    sender = "your_email@gmail.com"
    password = "your_password"
    receiver = "recipient_email@gmail.com"

    msg = MIMEText(message)
    msg['Subject'] = "Currency Rate Alert"
    msg['From'] = sender
    msg['To'] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("Email alert sent successfully.")
    except Exception as e:
        print(f"Email alert could not be sent. Error: {str(e)}")

@agent.on_interval(period=28800.0)
async def time_interval(ctx: Context):
    check_thresholds()

if __name__ == '__main__':
    fund_agent_if_low(agent)
    agent.run()
