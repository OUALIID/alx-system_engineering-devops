#!/usr/bin/python3
"""
0x16-api_advanced
"""
import requests


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the titles
    of the first 10 top posts listed on a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(
        url,
        headers={"User-Agent": "custom"}
    )
    if response.status_code == 200:
        for item in response.json()["data"]["children"]:
            print(item["data"]["title"])
    else:
        print(None)
