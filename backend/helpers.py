# The rest of your Flask application logic and routes would be here
import os
import urllib.parse
from functools import wraps

import requests
from dotenv import load_dotenv
from flask import redirect, render_template, request, session


def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        url = f"https://api.twelvedata.com/quote?symbol={symbol}&apikey={api_key}"  # Use the provided symbol parameter
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["name"],  # Use "name" instead of "companyName" if available
            "price": float(
                quote["close"]
            ),  # Use "close" instead of "latestPrice" if available
            "symbol": quote["symbol"],
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


def is_int(s):
    """check if the input is an integer"""
    try:
        int(s)
        return True
    except ValueError:
        return False
