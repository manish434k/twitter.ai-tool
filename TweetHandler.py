import tweepy

# keys and tokens from the Twitter Developer Dashboard
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
bearer = r""


# Authenticate to Twitter
client = tweepy.Client(bearer, consumer_key, consumer_secret, access_token, access_token_secret)

# set up OAuth and integrate with API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#Post a tweet
#client.create_tweet(text="The stock market is filled with individuals who know the price of everything, but the value of nothing. — Philip Fisher")


"""
Post a tweet to Twitter.

Args:
    tweetTxt (str): The text of the tweet to be posted.

Raises:
    ValueError: If the tweet is empty, longer than 280 characters.
    ValueError: If the tweet starts with 'RT @' or 'Dear Hive users'.

Returns:
    None
"""
def post_tweet(tweetTxt):
    if len(tweetTxt) == 0:
        raise ValueError("Tweet cannot be empty")
    elif len(tweetTxt) > 280:
        raise ValueError("Tweet too long, 280 characters max")
    else:
        print("Posting tweet: " + tweetTxt)
        client.create_tweet(text=tweetTxt)


       
