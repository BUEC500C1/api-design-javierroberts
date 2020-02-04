import tweepy
import keys


def getFeed():
    auth = tweepy.OAuthHandler(keys.key, keys.skey)
    auth.set_access_token(keys.token, keys.stoken)

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


if __name__ == "__main__":
    getFeed()
