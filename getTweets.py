from fetchTweets import *
from sentimentDetection import *
from wordCoud import generate_wc
from treeMap import *


def get_all_tweets(start_date, end_date):
    tweets_analyser = []
    tweet_cnn = tweetFetch('@cnnbrk', start_date, end_date)
    tweet_bbc = tweetFetch('@bbcbreaking', start_date, end_date)
    tweet_nyn = tweetFetch('@nytimes', start_date, end_date)
    total_tweets = tweet_cnn + tweet_bbc + tweet_nyn
    print("length ::" , len(total_tweets))

    ptweets, netweets, ntweets = "", "", ""

    for tweet in total_tweets:
        text = (tweet.text.split("http")[0]).replace("…", "")

        nwtweets, tweet_1 = get_tweet_sentiment(text)
        tweets_analyser.append(tweet_1)
        print(
            "-------------------------------------------------------------------------------------------------------------")
        print(" Twitter Highlight: ", tweet.text.replace("\n", " "))
        print(" Sentiment   : ", nwtweets)
        if nwtweets == "positive":
            ptweets = ptweets + str(tweet_1)
        elif nwtweets == "neutral":
            netweets = netweets + str(tweet_1)
        else:
            ntweets = ntweets + str(tweet_1)

    generate_wc(netweets, ptweets, ntweets)
    country_analysis(tweets_analyser)
    return "Success"
