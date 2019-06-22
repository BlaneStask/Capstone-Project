import tweepy
import json


# fetch the secrets from our virtual environment variables
CONSUMER_KEY = ["CONSUMER_KEY"]
CONSUMER_SECRET = ["CONSUMER_SECRET"]
ACCESS_TOKEN = ["ACCESS_TOKEN"]
ACCESS_SECRET = ["ACCESS_SECRET"]
# authenticate to the service we're accessing
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# create the connection
api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search,
            q="python",
            lang="en",
            since=2018-11-16).items(5)

status = api.user_timeline(user=bstaskiewicz, count=1)[0]
json.dumps(status)


def avg_tweet(tweets):
    total = 0
    y = 1
    for tweet in tweets:
        num = len(tweet['text'])
        total = num + total
        y += 1

    return total / y


#print("The average tweet length is: ", avg_tweet(tweets))


def find_longest_word(tweets):
    longest_word = ''
    for tweet in tweets:
        text = tweet['text'].split()
        for word in text:
            if len(word) > len(longest_word):
                longest_word = word

    return longest_word


#print("The longest word in a single tweet is: ", find_longest_word(tweets))


def users(tweets):
    total = 0
    y = 1
    for tweet in tweets:
        user = tweet['user']['followers_count']
        total = user + total
        y += 1
    return total / y


#print("The average number of followers are: ", users(tweets))
