import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    # fetch the secrets from our virtual environment variables
    consumer_key = os.environ["CONSUMER_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    access_token = os.environ["ACCESS_TOKEN"]
    access_secret = os.environ["ACCESS_SECRET"]
    # authenticate to the service we're accessing
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # create the connection
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

logging.basicConfig(level=logging.INFO)

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self:
            return
        try:
            tweet.favorite()
            tweet.retweet()
        except Exception as e:
            logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)

def main(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])

if __name__ == "__main__":
    main(["Tesla"])
