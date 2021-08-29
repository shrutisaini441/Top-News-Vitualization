from textblob import TextBlob
import re


def get_tweet_sentiment(tweet):
    # A TextBlob Object is created
    analysis = TextBlob(clean_tweet(tweet))
    # Identifying the Polarity
    if analysis.sentiment.polarity > 0:
        return 'positive', analysis
    elif analysis.sentiment.polarity == 0:
        return 'neutral', analysis
    else:
        return 'negative', analysis


def clean_tweet(tweet):
    # Cleaning of the tweets fetched
    final = ""
    clean_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w+:r'\ / \ / \S+)", " ", tweet).split())
    for cleanTw in clean_text.split(" "):
        if len(cleanTw) < 4 or "RT" in cleanTw or cleanTw == "#" or "RTS" in cleanTw:
            pass
        else:
            final = final + " " + cleanTw
    return final
