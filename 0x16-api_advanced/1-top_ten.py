#!/usr/bin/python3
""" Print the titles of the first 10 hot posts for a given subreddit. """
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    
    Returns:
        None: Prints the titles of the posts or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                print(post['data'].get('title', ''))
        else:
            print(None)
    except requests.RequestException:
        print(None)
