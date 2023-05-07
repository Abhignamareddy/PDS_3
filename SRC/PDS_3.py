#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read the CSV file (Corona_NLP_test.csv) containing the tweets into a DataFrame called data
data = pd.read_csv('../data_raw/Corona_NLP_test.csv')

# Select the 'OriginalTweet' column as the text corpus
text_corpus = data['OriginalTweet']

# a) Tokenize the text corpus
# Split the text corpus into individual words using the word_tokenize() function from NLTK.
# Store the tokens in a list called tokens
tokens = []
for text in text_corpus:
    tokens.extend(word_tokenize(text))

# Function to clean the tokens by removing special characters
def clean_str(x):
    # Define a string containing all special characters to be removed
    special_chars = '`!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}—~“”’'
    # Convert to lowercase
    lowercased_str = x.lower()
    # Remove each special character in the string
    for ch in special_chars:
        lowercased_str = lowercased_str.replace(ch, '')
    return lowercased_str

# b) Remove stop words from the tokens
# Create a set of stop words from the NLTK stopwords corpus
stop_words = set(stopwords.words('english'))
# Remove tokens that are in the stop words set or are not alphabetic.
# Store the cleaned tokens in a new list called tokens_after_stop_words_removal
tokens_after_stop_words_removal = [clean_str(token) for token in tokens if token not in stop_words and token.isalpha()]

# c) Count the frequencies of each token in the cleaned token list
# Use the Counter() function to count the frequencies of each token in the cleaned token list.
# The result is stored in a Counter object called word_counts.
word_counts = Counter(tokens_after_stop_words_removal)

# d) Generate a word cloud from the token frequencies
# Create a WordCloud object with a white background.
# Generate the word cloud visualization from the word frequencies using generate_from_frequencies().
wordcloud = WordCloud(width=800, height=800, background_color='white').generate_from_frequencies(word_counts)
# Plot the word cloud
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('../results/wordcloud.png')
plt.show()


# In[ ]:




