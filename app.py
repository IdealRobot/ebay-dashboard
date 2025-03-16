"""
Ebay Store Manager - Dashboard Application
-------------------------------------------
Author: John Szpyrka
Date: 142251MAR2025
Description:
This is the core Flask application for the Ebay Store Manager project. It serves
as the entry point for managing eBay store metrics, integrating with the eBay API,
and displaying key business insights in a user-friendly dashboard.

Routes:
- '/' : Homepage displaying basic app info (to be expanded with dashboard features).

Future Enhancements:
- Add metrics dashboard with eBay API integration.
- Implement data caching for performance.
- Build dynamic date range selectors for enhanced reporting.
"""

import requests
import os
from dotenv import load_dotenv
from flask import Flask, render_template

# Load environment variables
load_dotenv()

app = Flask(__name__)

EBAY_API_URL = "https://api.ebay.com/sell/fulfillment/v1/order"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('EBAY_PROD_TOKEN')}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

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
    """Home route that fetches and displays orders."""
    try:
        all_orders = fetch_all_orders()
        metrics = {
            "Total Orders (90 days)": len(all_orders)
        }
        # Print pricing summary for each of the first 10 orders
        print("First 10 orders' pricing summary:")
        for order in all_orders[:10]:
            print(order.get('pricingSummary'))
    except Exception as e:
        metrics = {"Total Orders (90 days)": 0}
        print(f"An error occurred: {e}")

    return render_template('index.html', metrics=metrics, orders=all_orders)

if __name__ == '__main__':
    app.run(debug=True)
