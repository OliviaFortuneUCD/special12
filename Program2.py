import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
example_string = "Hello my name is Olivia, How are you today?"
print(sent_tokenize(example_string))

EXAMPLE_TEXT = "An an valley indeed so no wonder future nature vanity. " \
               "Debating all she mistaken indulged believed provided declared. He many kept on draw lain song as same. Whether at dearest certain spirits is entered in to. Rich fine bred real use too many good. She compliment unaffected expression favourable any. Unknown chiefly showing to conduct no."
frequency = nltk.FreqDist(EXAMPLE_TEXT)
for key,val in frequency.items():
    print (str(key) + ':' + str(val))



import re
text = "Please contact us at contact@blahblah.com for further information."+\
        " You can also give feedback at feedback@blah.com"


emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print (emails)

#stop words

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)


