#importing the required libraries & packages
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


df= pd.read_csv("Tweets.csv")
print(df.head())

print("Shape of the dataframe is",df.shape)
print("The number of nulls in each column are \n", df.isna().sum())

print("Percentage null or na values in df")
((df.isnull() | df.isna()).sum() * 100 / df.index.size).round(2)

#the following have missing data, get rid
del df['tweet_coord']
del df['airline_sentiment_gold']
del df['negativereason_gold']
df.head()

print("Total number of tweets for each airline \n ",df.groupby('airline')['airline_sentiment'].count().sort_values(ascending=False))
airlines= ['US Airways','United','American','Southwest','Delta','Virgin America']


