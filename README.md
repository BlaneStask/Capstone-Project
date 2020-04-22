# Capstone Project

This is the Capstone Project for the CodingNomads Python Course. 

In this project I gather data from Twitter using Tweepy, make a Twitter Bot, and use functions to find:

- The average number of followers.
- The average length of tweets (counting words).
- The average length of tweets (counting characters).
- The percentage of tweets that have a hashtag (#).
- The percentage of tweets that have a mention (@).
- The 100 most common words.
- The 100 most common symbols.
- Percentage of tweets that use punctuation.
- The longest word in a tweet.
- Shortest word in a tweet.
- What user has the most tweets in the dataset.
- The average number of tweets from an individual user.
- The hour with the greatest number of tweets.

## Modules Used

```Python
import tweepy
import os
import collections
import sqlalchemy
import pymysql
from time import gmtime, strftime
from pprint import pprint
```
## Example Functions

An example function from capstone.py , the most common symbols:

```python
def common_symbols(tweets):
    char_count = {}
    print("The 100 most common symbols are: ")
    for tweet in tweets:
        text = tweet.text
        for char in text:
            if char.isalpha() == False and char.isdigit() == False:
                if char not in char_count:
                    char_count[char] = 1
                else:
                    char_count[char] += 1
    char_counter = collections.Counter(char_count)
    for char, count in char_counter.most_common():
        print(char, ": ", count)
```

And the user with the most tweets:

```python
def most_tweets(tweets):
    most_user_tweets = 0
    user_name = ' '
    print("The user with the most amount of tweets and retweets is: ")
    for tweet in tweets:
        user = tweet.user.screen_name
        user_tweets = tweet.user.statuses_count
        if user_tweets > most_user_tweets:
            most_user_tweets = user_tweets
            user_name = user
    print(user_name, " with ", most_user_tweets)
```

