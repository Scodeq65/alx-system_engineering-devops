#!/usr/bin/python3
"""Queries the Reddit API recursively to get all hot articles for a given
subreddit."""
import requests


def recurse(subreddit, hot_list=[]):
    """Recursively queries the Reddit API and returns a list of all hot
    articles' titles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): Accumulator list to store the titles of hot articles.

    Returns:
        list: A list of titles of all hot articles or None if the subreddit is
              invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after', None)

        if not posts:
            return hot_list if hot_list else None

        for post in posts:
            title = post['data'].get('title')
            if title:
                hot_list.append(title)

        if after:
            # Recursive call with the next page of results
            return recurse(subreddit, hot_list)

        return hot_list

    except requests.RequestException:
        return None
