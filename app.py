"""
Ebay Store Manager - Dashboard Application (v1.1)
--------------------------------------------------
Author: John Szpyrka
Date: 152330MAR2025
Description:
This is the core Flask application for the Ebay Store Manager project. It serves as the entry point for managing eBay store metrics, integrating with the eBay API, and displaying key business insights in a user-friendly dashboard.

Updates in this version:
- Refactored to use Waitress as the WSGI server for production readiness.
- Implemented logic to calculate and display total orders over the last 30, 60, and 90 days.

Routes:
- '/' : Homepage displaying total orders metrics for the last 30, 60, and 90 days.

Future Enhancements:
- Add a more comprehensive metrics dashboard with additional eBay API integrations.
- Implement data caching for improved performance.
- Build dynamic date range selectors for enhanced reporting.
"""

import requests
import os
from dotenv import load_dotenv
from flask import Flask, render_template
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

app = Flask(__name__)

EBAY_API_URL = "https://api.ebay.com/sell/fulfillment/v1/order"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('EBAY_PROD_TOKEN')}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

print("EBAY_PROD_TOKEN Loaded:", os.getenv('EBAY_PROD_TOKEN'))

def fetch_all_orders():
    """Fetch all orders from the eBay API."""
    params = {
        "limit": 200,
        "offset": 0,
        "order_status": "ALL"
    }
    response = requests.get(EBAY_API_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("orders", [])

@app.route('/')
def home():
    """Home route that calculates orders from the last 30, 60, and 90 days."""
    try:
        # Fetch all orders from the eBay API.
        all_orders = fetch_all_orders()
        
        # Define date thresholds.
        now = datetime.now()
        threshold_30 = now - timedelta(days=30)
        threshold_60 = now - timedelta(days=60)
        threshold_90 = now - timedelta(days=90)
        
        # Initialize counts.
        count_30 = 0
        count_60 = 0
        count_90 = 0
        
        # Iterate over orders and count those within each period.
        for order in all_orders:
            creation_date_str = order.get("creationDate", "")
            if creation_date_str:
                try:
                    # Remove trailing 'Z' (if present) and parse the date.
                    creation_date = datetime.fromisoformat(creation_date_str.rstrip("Z"))
                    if creation_date >= threshold_30:
                        count_30 += 1
                    if creation_date >= threshold_60:
                        count_60 += 1
                    if creation_date >= threshold_90:
                        count_90 += 1
                except Exception as parse_error:
                    print(f"Failed to parse creation date: {parse_error}")
                    continue
        
        metrics = {
            "30": count_30,
            "60": count_60,
            "90": count_90
        }
    except Exception as e:
        metrics = {"30": 0, "60": 0, "90": 0}
        print(f"An error occurred: {e}")

    return render_template('index.html', metrics=metrics)

from waitress import serve

print("Starting script...")

if __name__ == '__main__':
    print("Reached the entry point.")
    print("Starting Waitress server...")
    try:
        serve(app, host='0.0.0.0', port=8000)
        print("Waitress server started successfully.")
    except Exception as e:
        print(f"Failed to start Waitress server: {e}")
