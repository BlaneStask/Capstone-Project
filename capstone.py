import tweepy
import os
import collections
import pandas as pd
import numpy as np
import sqlalchemy
import pymysql
from time import gmtime, strftime
from pprint import pprint

# fetch the secrets from our virtual environment variables
CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]
# authenticate to the service we're accessing
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# create the connection
api = tweepy.API(auth)

tweets = [i for i in tweepy.Cursor(api.search,
            q="python",
            lang="en",
            since=2019-6-29).items(100)]


status = api.user_timeline(user="bstaskiewicz", count=1)[0]


def avg_tweet_word(tweets):
    total = 0
    total_tweets = len(tweets)
    for tweet in tweets:
        text = tweet.text.split()
        for word in text:
            total += 1

    return total / total_tweets


print("The average tweet length by word is: ", avg_tweet_word(tweets))


def find_longest_word(tweets):
    longest_word = ' '
    print("The longest words in the tweets are: ")
    for tweet in tweets:
        text = tweet.text.split()
        for word in text:
            if len(word) > len(longest_word):
                longest_word = word
        print(longest_word)
        longest_word = ' '


find_longest_word(tweets)


def users(tweets):
    total = 0
    all_users = 0
    for tweet in tweets:
        user = tweet.user.followers_count
        total += user
        all_users += 1
    return total / all_users


print("The average number of followers are: ", users(tweets))


def avg_tweet_char(tweets):
    total = 0
    total_tweets = len(tweets)
    for tweet in tweets:
        text = tweet.text
        for char in text:
            if char != ' ' and char != ',' and char != '.' and char != "'":
                total += 1

    return total / total_tweets


print("The average tweet length by char is: ", avg_tweet_char(tweets))


def percent_w_ht(tweets):
    total = 0
    total_tweets = len(tweets)
    one_p_t = 0
    for tweet in tweets:
        text = tweet.text.split()
        for word in text:
            for char in word:
                if char == '#' and one_p_t == 0:
                    total += 1
                    one_p_t = 1
        one_p_t = 0
    div = total / total_tweets
    percent = div * 100
    return percent


print("The percent of tweets with an # are: ", percent_w_ht(tweets))


def percent_w_as(tweets):
    total = 0
    total_tweets = len(tweets)
    one_p_t = 0
    for tweet in tweets:
        text = tweet.text.split()
        for word in text:
            for char in word:
                if char == '@' and one_p_t == 0:
                    total += 1
                    one_p_t = 1
        one_p_t = 0
    div = total / total_tweets
    percent = div * 100
    return percent


print("The percent of tweets with a @ are: ", percent_w_as(tweets))


def percent_w_p(tweets):
    total = 0
    total_tweets = len(tweets)
    one_p_t = 0
    for tweet in tweets:
        text = tweet.text
        for word in text:
            for char in word:
                if char == '.' or char == ',' or char == '/' or char == "'" or char == '!' or char == '?' and one_p_t == 0:
                    total += 1
                    one_p_t = 1
                elif char == ')' or char == '[' or char == ']' or char == '*' or char == '-' and one_p_t == 0:
                    total += 1
                    one_p_t = 1
                elif char == ';' or char == '"' or char == '(' or char == ':' or char == '_' and one_p_t == 0:
                    total += 1
                    one_p_t = 1
        one_p_t = 0
    div = total / total_tweets
    percent = div * 100
    return percent


print("The percent of tweets with punctuation are: ", percent_w_ht(tweets))


def find_shortest_word(tweets):
    shortest_word = '     '
    print("The shortest words in the tweets are: ")
    for tweet in tweets:
        text = tweet.text.split()
        for word in text:
            if len(word) <= len(shortest_word):
                shortest_word = word
        print(shortest_word)
        shortest_word = 'four'


find_shortest_word(tweets)


def common_words(tweets):
    wordcount = {}
    print("The 100 most common words are: ")
    for tweet in tweets:
        text = tweet.text.split()
        for word in text:
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            word = word.replace("\"", "")
            word = word.replace("!", "")
            word = word.replace("â€œ", "")
            word = word.replace("â€˜", "")
            word = word.replace("*", "")
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common():
        print(word, ": ", count)


common_words(tweets)


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


common_symbols(tweets)


def most_tweets(tweets):
    most_user_t = 0
    user_name = ' '
    print("The user with the most amount of tweets and retweets is: ")
    for tweet in tweets:
        user = tweet.user.screen_name
        user_t = tweet.user.statuses_count
        if user_t > most_user_t:
            most_user_t = user_t
            user_name = user
    print(user_name, " with ", most_user_t)


most_tweets(tweets)


def avg_num_tweets(tweets):
    total = 0
    all_tweets = 0
    print("The average number of tweets and retweets is: ")
    for tweet in tweets:
        user_t = tweet.user.statuses_count
        total += user_t
        all_tweets += 1
    val = total / all_tweets
    print(val)


avg_num_tweets(tweets)


def most_common_hour(tweets):
    hours = {}
    series = [tweet.user.created_at.strftime('%H') for tweet in tweets]
    for hour in series:
        if hour in hours:
            hours[hour] += 1
        else:
            hours[hour] = 1
    top_hour = max(hours, key=hours.get)
    return top_hour


print("The hour with the greatest number of tweets is: ", most_common_hour(tweets))


engine = sqlalchemy.create_engine('mysql+pymysql://root:mydogisachub9336@localhost/Twitter_Data')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

twitter_data = sqlalchemy.Table('Twitter Data', metadata,
                            sqlalchemy.column('created_at', sqlalchemy.DateTime(40)),
                            sqlalchemy.column('id', sqlalchemy.Integer()),
                            sqlalchemy.column('id_str', sqlalchemy.Integer()),
                            sqlalchemy.column('text', sqlalchemy.String(200)),
                            sqlalchemy.column('expanded_url', sqlalchemy.String(100)),
                            sqlalchemy.column('user_name', sqlalchemy.String(20)),
                            sqlalchemy.column('followers_count', sqlalchemy.Integer()),
                            sqlalchemy.column('statuses_count', sqlalchemy.Integer()),
                            sqlalchemy.column('active', sqlalchemy.Boolean()))
                            
twitter_data_results = sqlalchemy.Table('Twitter Data Results', metadata,
                            sqlalchemy.column('avg_tweet_length_word', sqlalchemy.Integer()),
                            sqlalchemy.column('longest_words', sqlalchemy.JSON(200)),
                            sqlalchemy.column('avg_num_followers', sqlalchemy.Integer()),
                            sqlalchemy.column('avg_tweet_length_char', sqlalchemy.Integer()),
                            sqlalchemy.column('percent_wit_#', sqlalchemy.Integer()),
                            sqlalchemy.column('percent_wit_@', sqlalchemy.Integer()),
                            sqlalchemy.column('percent_wit_punctuation', sqlalchemy.Integer()),
                            sqlalchemy.column('shortest_words', sqlalchemy.JSON(300)),
                            sqlalchemy.column('100_common_sym', sqlalchemy.JSON(300)),
                            sqlalchemy.column('user_most_tweets', sqlalchemy.JSON(50)),
                            sqlalchemy.column('avg_num_tweets', sqlalchemy.Integer()),
                            sqlalchemy.column('hour_most_tweets', sqlalchemy.Integer()),
                            sqlalchemy.column('100_common_words', sqlalchemy.JSON(300)))

metadata.creat_all(engine)

query = sqlalchemy.insert(twitter_data).values(tweets)
result_proxy = connection.execute(query)


def insert_results():
    func = [avg_num_tweets(tweets), avg_tweet_char(tweets), avg_tweet_word(tweets), find_shortest_word(tweets),
            find_longest_word(tweets), users(tweets), percent_w_p(tweets), percent_w_as(tweets), percent_w_ht(tweets),
            common_words(tweets), common_symbols(tweets), most_tweets(tweets), most_common_hour(tweets)]
    for results in func:
        query2 = sqlalchemy.insert(twitter_data_results).values(results)
        connection.execute(query2)


insert_results()


def select_results():
    func = [avg_num_tweets(tweets), avg_tweet_char(tweets), avg_tweet_word(tweets), find_shortest_word(tweets),
            find_longest_word(tweets), users(tweets), percent_w_p(tweets), percent_w_as(tweets), percent_w_ht(tweets),
            common_words(tweets), common_symbols(tweets), most_tweets(tweets), most_common_hour(tweets)]
    for results in func:
        query3 = sqlalchemy.select(twitter_data_results).values(results)
        pprint(query3)


#select_results()
