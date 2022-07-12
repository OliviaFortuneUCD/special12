#importing the required libraries & packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from wordcloud import WordCloud,STOPWORDS


df=pd.read_csv("Tweets.csv")
airlines= ['US Airways','United','American','Southwest','Delta','Virgin America']

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

# get the number of negative reasons
df['negativereason'].nunique()

NR_Count = dict(df['negativereason'].value_counts(sort=False))


def NR_Count(Airline):
    if Airline == 'All':
        a = df
    else:
        a = df[df['airline'] == Airline]
    count = dict(a['negativereason'].value_counts())
    Unique_reason = list(df['negativereason'].unique())
    Unique_reason = [x for x in Unique_reason if str(x) != 'nan']
    Reason_frame = pd.DataFrame({'Reasons': Unique_reason})
    Reason_frame['count'] = Reason_frame['Reasons'].apply(lambda x: count[x])
    return Reason_frame


def plot_reason(Airline):
    a = NR_Count(Airline)
    count = a['count']
    Index = range(1, (len(a) + 1))
    plt.bar(Index, count,
            color=['red', 'yellow', 'blue', 'green', 'black', 'brown', 'gray', 'cyan', 'purple', 'orange'])
    plt.xticks(Index, a['Reasons'], rotation=90)
    plt.ylabel('Count')
    plt.xlabel('Reason')
    plt.title('Count of Reasons for ' + Airline)


plot_reason('All')
plt.figure(2, figsize=(13, 13))
for i in airlines:
    indices = airlines.index(i)
    plt.subplot(2, 3, indices + 1)
    plt.subplots_adjust(hspace=0.9)
    plot_reason(i)