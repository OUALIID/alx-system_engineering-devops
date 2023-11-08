#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns
    the number of subscribers to a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(
        url,
        headers={"User-Agent": "custom"}
    )
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0
