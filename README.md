# 🌧️ Rain Alert

A Python script that checks the weather forecast for your location every hour and sends you an email (and optionally an SMS via Twilio) letting you know if it's going to rain in the next 12 hours.

## What it does

- Fetches hourly precipitation data from the [Open-Meteo API](https://open-meteo.com/) for your specified coordinates
- Checks if any precipitation is expected in the next 12 hours
- Sends an email alert via Gmail SMTP — either a rain warning or an all-clear message
- Optionally sends an SMS alert via Twilio
- Runs on an hourly loop

## Setup

1. Clone the repo
2. Install dependencies:
```
pip install openmeteo-requests requests-cache retry-requests pandas twilio
```
3. Open `main.py` and fill in your credentials:
   - `mail` — your Gmail address
   - `mail_2` — the recipient email
   - `pw` — your Gmail app password
   - `weather_params` — set your `latitude` and `longitude` ("www.latlong.net")
   - Twilio credentials (optional, SMS section is commented out by default)

## Notes

- Uses [Open-Meteo](https://open-meteo.com/) — no API key required for weather data
- Gmail requires an [App Password](https://support.google.com/accounts/answer/185833) (not your regular password)
- Twilio SMS is optional — the SMS section can be uncommented if you have an account
