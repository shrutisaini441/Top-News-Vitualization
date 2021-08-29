import tweepy
import datetime

consumer_key = 'X0D1jff0N2mWinpzrrWIs0imO'
consumer_secret = 'BZmN5lb4K0WyBMXkGuk8nkNk3udDSMuH0cOeEey7A6vcgX4W04'
access_key = '1363701203562074112-FGwl5NiA3Za9avSzdSKchPXztQ3Rg6'
access_secret = 'dRLvik00H2CzYIfEaW29N2Tgnxy1o8BFqR6IUQLvx85Gs'


def tweetFetch(screen_name , start_date , end_date):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    startDate = datetime.datetime(start_date.year, start_date.month, start_date.day, 00, 00, 00)
    endDate = datetime.datetime(end_date.year, end_date.month, end_date.day, 00, 00, 00)
    api = tweepy.API(auth)

    tweets = []
    tmpTweets = api.user_timeline(screen_name)
    for tweet in tmpTweets:
        if (tweet.created_at < endDate) and (tweet.created_at > startDate):
            tweets.append(tweet)
    # print(" start date" , startDate , "end date " , endDate)

    while tmpTweets[-1].created_at > startDate:
        tmpTweets = api.user_timeline(screen_name, max_id=tmpTweets[-1].id)
        for tweet in tmpTweets:
            if (tweet.created_at < endDate) and (tweet.created_at > startDate):
                tweets.append(tweet)
    return tweets