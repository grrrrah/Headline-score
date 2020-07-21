# Headline-score

This project uses data scraped from links coming from tweets. The script which does the scraping is available under news_scrape.py. Usually news outlets post a link to the certain piece of news of which the tweet contains a short summary. 
Parts of this data can be made available on demand as my project uses a large amount of data and cannot be uploaded here. The methods used in order to calculate a presupposed relevance
of the headline to the content of the news is available here.
In order to measure the semantic similarity between two strings of words there are several steps to be taken. A machine needs to work with vectorial representations of words encoding information about their distribution and meaning. Measurements cannot be conducted on plain alphabetical strings. Three types of word embeddings are used in my project: a document-term matrix containing the token counts, a 'sparse' training of a neural network by repeatedly iterating over a training corpus which outputs multidimensional vectors and another word co-occurrence matrix. Two types of extractive summarization algorithms are used too: one which uses a LSTM network and K-Means clustering and another one which uses the TextRank algorithm.
	4.1 Document-term matrix  + Cosine Distance
	4.2 Neural Network based embeddings(Doc2Vec) + TextRank Summarization + Cosine Distance
	4.3 Co-occurrence matrix(Glove) + BERT Summarization + Cosine Distance;
