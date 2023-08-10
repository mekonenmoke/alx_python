#!/usr/bin/python3
"""A script that
takes in a URL, sends a request to the URL and displays the value of the variable
"""


import requests
import sys


def fetch_and_display_x_request_id(url):
    """
    Fetches the X-Request-Id header value from the response of a given URL.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    response = requests.get(url)

    if response.status_code == 200:
        x_request_id = response.headers.get("X-Request-Id")
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
    else:
        print("Failed to fetch the URL. Status code:", response.status_code)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python xx.py <URL>")
    else:
        target_url = sys.argv[1]
        fetch_and_display_x_request_id(target_url)
