import pandas as pd
movies_imdb = pd.read_csv("IMDB_sample.csv")
print(movies_imdb.shape)
movies_imdb.head()

# Find the number of positive and negative reviews
print('Number of positive and negative reviews: ', movies_imdb.label.value_counts())

# Find the proportion of positive and negative reviews
print('Proportion of positive and negative reviews: ', movies_imdb.label.value_counts() / len(movies_imdb))



