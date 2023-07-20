# Amazon-pricetracker

Amazon Price Tracker in Python

The Amazon Price Tracker is a Python script that allows users to track the price of a product on Amazon by providing its link as input. The script fetches the product's current price from the Amazon website, keeps a record of the price history in an Excel file, and notifies the user via email if the price falls below the desired price set by the user.

Features:

Input: Users can input the Amazon product link they wish to track and set their desired price for the product.
Web Scraping: The script utilizes web scraping techniques to extract the current price of the product from the Amazon website using libraries such as Beautiful Soup and Requests.
Price History: The script maintains a historical record of the product's prices in an Excel file. Each time the script runs, it appends the new price and timestamp to the Excel file, creating a price tracking history.
Price Alert: If the current price of the product drops below the desired price set by the user, the script automatically sends an email notification to the user using the SMTP library in Python.
Email Customization: The user can customize the email notification, including the subject, body, and sender's email address.
Usage:

Run the script and provide the Amazon product link and desired price as inputs.
The script will fetch the current price, compare it with the desired price, and notify the user via email if the price drops below the specified amount.
The price history will be recorded and saved in an Excel file, allowing users to review the product's price trends over time.

Dependencies:
Python 3.x
Beautiful Soup
Requests
Pandas
Openpyxl
SMTP Library
Note:
It is essential to use web scraping responsibly and respect Amazon's terms of service. Ensure that the scraping is done in a manner that does not overload the servers or violate any usage policies.

This Amazon Price Tracker in Python provides a convenient and automated way for users to monitor price fluctuations and make informed purchasing decisions on Amazon products while staying within their budget.
