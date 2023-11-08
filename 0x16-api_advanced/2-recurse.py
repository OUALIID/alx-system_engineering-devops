#!/usr/bin/python3
"""
0x16-api_advanced
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    if count >= 10:
        return hot_list

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "&after={}".format(after)
    response = requests.get(
        url,
        headers={"User-Agent": "custom"}
    )

    if response.status_code == 200:
        if not response.json()["data"]["children"]:
            return None

        for item in response.json()["data"]["children"]:
            hot_list.append(item["data"]["title"])

        if after:
            return recurse(subreddit, hot_list, after, count + 1)

    return hot_list
