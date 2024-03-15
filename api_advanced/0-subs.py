#!/usr/bin/python3
"""Return number of subscribers for a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

# Test cases
def test_existing_subreddit():
    assert number_of_subscribers("python") == 757426

def test_non_existing_subreddit():
    assert number_of_subscribers("thissubredditdoesnotexist123") == 0

# Module-level test runner
if __name__ == "__main__":
    test_existing_subreddit()
    test_non_existing_subreddit()
    print("All tests passed.")
