# Currency_

markdown

# Currency Exchange Monitor with Email Alerts

This Python script monitors the exchange rate between two currencies and sends email alerts when the rate falls below a specified threshold. It uses the `forex-python` library to fetch exchange rate data and the `smtplib` library to send email notifications.

## Prerequisites

Before running the script, ensure you have the following prerequisites:

- Python 3.x installed on your system.
- The `forex-python` library, which can be installed using `pip`:

  ```bash
  ## pip install forex-python

Configuration

    Open the currency_exchange_monitor.py file.

    Replace the following placeholders with your own details:
        SMTP_SERVER: Your SMTP server address (e.g., 'smtp.example.com').
        SMTP_PORT: The SMTP server port (e.g., 587 for TLS).
        YOUR_EMAIL: Your email address for sending alerts.
        YOUR_EMAIL_PASSWORD: Your email password (Consider using an app-specific password for security).
        RECIPIENT_EMAIL: The recipient's email address for receiving alerts.
        BASE_CURRENCY: The currency you want to monitor (e.g., 'USD').
        TARGET_CURRENCY: The currency to which you want to convert (e.g., 'EUR').
        ALERT_THRESHOLD: The exchange rate threshold for sending alerts (e.g., 0.9 for 1 USD to EUR).

Usage

To start the currency exchange monitor, run the following command in your terminal:

bash

python currency_exchange_monitor.py

The script will continuously monitor the exchange rate and send email alerts when the rate falls below the specified threshold. It checks the rate every hour by default.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

    The script uses the forex-python library to retrieve exchange rate data. More information can be found here.
Readme is created using AI
