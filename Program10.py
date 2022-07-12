#importing the required libraries & packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from wordcloud import WordCloud,STOPWORDS


df=pd.read_csv("Tweets.csv")


new_df=df[df['airline_sentiment']=='positive']
words = ' '.join(new_df['text'])
cleaned_word = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])
wordcloud = WordCloud(stopwords=STOPWORDS,
                      background_color='black',
                      width=3000,
                      height=2500
                     ).generate(cleaned_word)


# Calculate highest frequency words in positive tweets
def freq(str):
    # break the string into list of words
    str = str.split()
    str2 = []

    # loop till string values present in list str
    for i in str:

        # checking for the duplicacy
        if i not in str2:
            # insert value in str2
            str2.append(i)

    for i in range(0, len(str2)):
        if (str.count(str2[i]) > 50):
            print('Frequency of', str2[i], 'is :', str.count(str2[i]))


print(freq(cleaned_word))