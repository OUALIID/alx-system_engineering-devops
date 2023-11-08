#!/usr/bin/python3
"""
0x16-api_advanced
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
        url,
        headers={"User-Agent": "custom"}
    )
    if response.status_code == 200:
        for item in response.json()["data"]["children"]:
            hot_list.append(item["data"]["title"])
    else:
        return None

    return hot_list
