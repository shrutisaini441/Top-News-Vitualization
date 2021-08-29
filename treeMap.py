import random
import matplotlib.pyplot as plt

plt.rcdefaults()
import seaborn as sns
import squarify
import nltk

nltk.download('punkt')
nltk.download('wordnet')
import pandas as pd
import re
import spacy

spacy.prefer_gpu()
nlp = spacy.load("en_core_web_sm")
from nltk.stem.snowball import SnowballStemmer

s_stemmer = SnowballStemmer(language='english')
from nltk.probability import FreqDist


def country_analysis(tweets_analyser):
    f = []
    for word in tweets_analyser:
        f.append(word)

    lines = list()
    for line in f:
        words = line.split()
        for w in words:
            lines.append(w)

            # print(lines)

    lines = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in lines]
    lines2 = []

    for word in lines:
        if word != '':
            lines2.append(word)

    stem = []
    for word in lines2:
        stem.append(s_stemmer.stem(word))
    # Removing all Stop Words

    stem2 = []

    for word in stem:
        if word not in nlp.Defaults.stop_words:
            stem2.append(word)

    # stem2
    df = pd.DataFrame(stem2)

    df = df[0].value_counts()

    freqdoctor = FreqDist()

    for words in df:
        freqdoctor[words] += 1

    str1 = " "
    stem2 = str1.join(lines2)

    stem2 = nlp(stem2)

    label = [(X.text, X.label_) for X in stem2.ents]

    df10 = pd.DataFrame(label, columns=['Word', 'Entity'])

    df10 = df10.where(df10['Entity'] == 'GPE')

    df11 = df10['Word'].value_counts()
    df = df11[:20, ]
    plt.figure(figsize=(10, 5))
    sns.barplot(df.values, df.index, alpha=0.8)
    plt.title('Top LOCATION Mentioned')
    plt.ylabel('Word from Tweet', fontsize=12)
    plt.xlabel('Count of Words', fontsize=12)
    plt.savefig('TreeMap/countryBarGraph.png')
    plt.show()
    colors = []
    for co in df.index:
        rgb = (random.random(), random.random(), random.random())
        colors.append(rgb)
    squarify.plot(sizes=df.values,
                  label=df.index,
                  alpha=0.8,
                  color=colors)
    plt.axis('off')
    plt.savefig('TreeMap/country.png')
    plt.show()
