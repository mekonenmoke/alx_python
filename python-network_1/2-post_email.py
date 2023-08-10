#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import requests
    import sys
    from urllib.parse import urlencode

    argv = sys.argv
    url = argv[1]
    email = argv[2]
    data = urlencode({"email": email})
    data = data.encode("ascii")

    response = requests.post(url, data=data)
    print("Your email is:", response.text)
