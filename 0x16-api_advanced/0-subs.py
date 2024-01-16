#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json().get("data", {})
        subscribers = data.get("subscribers", 0)
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

