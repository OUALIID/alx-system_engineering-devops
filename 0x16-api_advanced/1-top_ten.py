#!/usr/bin/python3
"""
0x16-api_advanced
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
        url,
        headers={"User-Agent": "custom"}
    )
    if requests == 200:
        return response.json()["data"]["title"]
    else:
        return 0