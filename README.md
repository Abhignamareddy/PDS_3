Tweets retrieved from Twitter are included in the data file Corona_NLP_test.csv.
Utilizing the textual information included in the "OriginalTweet" column of this dataset, performed the tasks listed below:

a) Create tokens from the text corpus.
  The text corpus was tokenized by using the word_tokenize() function included in the NLTK library to break it up into its component terms.
  
b) Remove any stop words.
  A new function called clean_str() has been added to strip each token of any special characters.
  The English language's stop words have been loaded with the help of the stopwords.words('english') function.
  The clean_str() method was called for each token while the iteration over the tokens was performed.
  Tokens that are not alphabetic or that are on a list of stop words have been eliminated.
  
c) Determine Word Frequency
  To get the number of times each token appears in the token list after it has been cleaned up, use the Counter() method included in the collections     module.
  
d) Create word clouds.
  The WordCloud object was given a white backdrop when it was created.
  Using the generate_from_frequencies() function, we created a visual representation of a word cloud using the word frequencies.
