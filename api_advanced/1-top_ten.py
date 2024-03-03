#!/usr/bin/python3
"""Queries the Reddit API and
prints the titles of the first
10 hot posts listed for a given
subreddit.
"""
import requests

def top_ten(subreddit):
    base_url = 'https://www.reddit.com'
    api_uri = f'{base_url}/r/{subreddit}/hot.json'
    user_agent = {'User-Agent': 'Python/requests'}
    payload = {'limit': '10'}

    res = requests.get(api_uri, headers=user_agent, params=payload, allow_redirects=False)

    if res.status_code == 200:  # If response is successful
        try:
            res_json = res.json()
            hot_posts = res_json['data']['children']
            for post in hot_posts:
                title = post['data']['title']
                print(title)
        except (KeyError, ValueError):
            print('Error: Unable to parse JSON response')
    elif res.status_code == 302:  # Handle redirect
        print('None')
    else:
        print(f"Error: Unexpected response code {res.status_code}")

