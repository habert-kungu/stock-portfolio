# Finance: A Stock Portfolio




![Screenshot from 2024-04-06 10-35-37](https://github.com/habert-kungu/stock-portfolio/assets/147383053/431016eb-15a9-40b2-9c2d-6b6639bb5f8d)


![Screenshot from 2024-04-06 10-36-33](https://github.com/habert-kungu/stock-portfolio/assets/147383053/2b8b3757-0221-4f25-92c7-b4a37d98afb1)


## Technologies
- Python
- Flask (with session authentication)
- SQL
- HTML
- Bootstrap

## Summary
Finance is a web app that allows logged-in users to manage a virtual stock portfolio. Users can "buy" and "sell" stocks with pretend money, look up real stock quotes fetched from the IEX API, and view their transaction history.

## How to Run
1. Clone this repository and navigate to the project directory.
2. Activate a virtual environment: `python3 -m venv .venv`, then activate it.
3. Install dependencies: `pip install -r requirements.txt`.
4. Set the Flask environment variable: `export FLASK_APP=application.py`.
5. Follow the instructions [here](https://cs50.harvard.edu/x/2020/tracks/web/finance/#configuring) to configure and export your API key.
6. Run the app: `flask run`.
7. Register for a new account on the finance site to create your stock portfolio.

## Views

### Register
Allows new users to register for an account. Renders an apology view if the form data is incomplete or if the username already exists in the database.

### Index
Displays a table of the logged-in user's owned stocks, including the number of shares, current stock price, and value of each holding. Also shows the user's imaginary "cash" balance and the total of their "cash" plus stock value.

### Quote
Allows users to look up a stock's current price by submitting a form. Retrieves real-time data from the IEX API. Renders an error message if the stock symbol is invalid.

### Buy
Enables users to "buy" stocks by submitting a form with the stock's symbol and number of shares. Checks if the stock symbol is valid and if the user can afford the purchase at the stock's current market price with their available balance. Stores the transaction history in the database.

### Sell
Allows users to "sell" shares of any stock currently owned in their portfolio.

### History
Displays a table summarizing the user's past transactions (buys and sells). Each row lists whether the stock was bought or sold, the stock's symbol, the buy/sell price, the number of shares, and the transaction date/time.

---
