#!/usr/bin/python3
"""Queries the Reddit API recursively to count occurrences of keywords in
hot articles' titles for a given subreddit and prints a sorted count."""
from collections import Counter
import re
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """Recursively queries the Reddit API to count occurrences of keywords in
    hot articles' titles and prints the sorted counts.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to count (case-insensitive).
        counts (Counter): Accumulator for keyword counts.
        after (str): Parameter for pagination.

    Returns:
        None: Prints the sorted counts or nothing if the subreddit is invalid.
    """
    if counts is None:
        counts = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(
            url, headers=headers, params={'after': after},
            allow_redirects=False
        )
        if response.status_code != 200:
            return None

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after', None)

        if not posts:
            sorted_counts = sorted(
                counts.items(), key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return

        word_list = [word.lower() for word in word_list]
        regex_pattern = re.compile(
            r'\b(?:' + '|'.join(map(re.escape, word_list)) + r')\b',
            re.IGNORECASE
        )

        for post in posts:
            title = post['data'].get('title', '')
            words = regex_pattern.findall(title)
            counts.update(word.lower() for word in words)

        if after:
            # Recursive call with the next page of results
            return count_words(subreddit, word_list, counts, after)

        sorted_counts = sorted(
            counts.items(), key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_counts:
            print(f"{word}: {count}")

    except requests.RequestException:
        return None
