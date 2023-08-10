#!/usr/bin/python3
"""A script that
fetches https://intranet.hbtn.io/status.
"""
import requests


def fetch_and_display_status(url):
    """
    Fetches the content from a given URL and displays information about the response.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        None
    """
    response = requests.get(url)

    if response.status_code == 200:
        print("Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text.strip())
    else:
        print("Failed to fetch the URL. Status code:", response.status_code)


if __name__ == "__main__":
    target_url = "https://alu-intranet.hbtn.io/status"
    fetch_and_display_status(target_url)
