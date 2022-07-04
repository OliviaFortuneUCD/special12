from nltk.tokenize import word_tokenize

import nltk

sagan_quote = """
If you wish to make an apple pie from scratch,
you must first invent the universe."""

words_in_sagan_quote = word_tokenize(sagan_quote)

print(nltk.pos_tag(words_in_sagan_quote))


#JJ	Adjectives
#NN	Nouns
#RB	Adverbs
#PRP	Pronouns
#VB	Verbs