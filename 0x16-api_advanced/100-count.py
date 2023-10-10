#!/usr/bin/python3
"""
 the Reddit API and prints
the top ten hot posts of a subreddit
"""
import re
import requests
import sys


def add_title(dictionary, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for wo in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(wo):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """ Queries to Reddit APIlistss """
    us_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': us_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """ Initialize the subredit api"""
    dictionary = {}

    for wo in word_list:
        dictionary[wo] = 0

    recurse(subreddit, dictionary)

    l = sorted(dictionary.items(), key=lambda kv: kv[1])
    l.reverse()

    if len(l) != 0:
        for items in l:
            if items[1] is not 0:
                print("{}: {}".format(items[0], items[1]))
    else:
        print("")
