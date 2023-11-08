#!/usr/bin/python3
"""
0x16. API advanced
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    if not subreddit:
        return None

    params = {"after": after} if after else {}
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={"User-Agent": "custom"},
        params=params
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])

    hot_list.extend(item["data"]["title"] for item in children)

    return recurse(subreddit, hot_list, after=data.get("after")) if data.get("after") else hot_list
