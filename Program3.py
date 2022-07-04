from nltk.tokenize import sent_tokenize, word_tokenize

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

quote = "I am going to Town on Tuesday, the weather is supposed to be good"

print(quote)

stop_words = set(stopwords.words("english"))

filtered_list = []

for word in quote:
   if word.casefold() not in stop_words:
        filtered_list.append(word)

  

filtered_list = [
    word for word in quote if word.casefold() not in stop_words
]
print(word)
