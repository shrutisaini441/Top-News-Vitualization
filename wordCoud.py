import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def generate_wc(netweets, ptweets, ntweets):
    # Word cloud for Neutral
    cloud1 = WordCloud(background_color="black", stopwords=STOPWORDS).generate(netweets)
    plt.imshow(cloud1)
    plt.axis('off')
    plt.savefig('WordCloud/neutral.png')
    plt.show()

    # Word cloud for Positive
    cloud2 = WordCloud(background_color="white", stopwords=STOPWORDS).generate(ptweets)
    plt.imshow(cloud2)
    plt.axis('off')
    plt.savefig('WordCloud/positive.png')
    plt.show()

    # Word cloud for Negative
    cloud3 = WordCloud(background_color="red", stopwords=STOPWORDS).generate(ntweets)
    plt.imshow(cloud3)
    plt.axis('off')
    plt.savefig('WordCloud/negative.png')
    plt.show()
