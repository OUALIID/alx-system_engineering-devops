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
        params = {"after": after}
    else:
        params = {}  # Initialize an empty parameter dictionary

    response = requests.get(
        url,
        headers={"User-Agent": "custom"},
        params=params  # Pass the query parameters here
    )

    if response.status_code == 200:
        data = response.json()["data"]
        children = data["children"]

        if not children:
            return hot_list

        for item in children:
            hot_list.append(item["data"]["title"])

        after = data["after"]
        return recurse(subreddit, hot_list, after, count + 1)

    return None  # Return None if the response status code is not 200

# Example usage:
if __name__ == '__main__':
    subreddit = "programming"  # Replace with your desired subreddit
    hot_articles = recurse(subreddit)
    if hot_articles is not None:
        print(len(hot_articles))
    else:
        print("None")
