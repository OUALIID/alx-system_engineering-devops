#!/usr/bin/python3
"""
0x16-api_advanced
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Recursively fetches hot article titles from a Reddit subreddit."""
    if count >= 10:
        return hot_list
    else:
        params = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        params = {"after": after}
    response = requests.get(
        url,
        headers={"User-Agent": "custom"},
        params=params
    )

    if response.status_code == 200:
        if not response.json()["data"]["children"]:
            return hot_list

        for item in response.json()["data"]["children"]:
            hot_list.append(item["data"]["title"])

        after = response.json()["data"]["after"]
        return recurse(subreddit, hot_list, after, count + 1)

    return None
