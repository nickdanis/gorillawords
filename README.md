# Predicting difficulty in NY Times Crossword puzzles

## [Erdős Code May 2021 Bootcamp](https://www.erdosinstitute.org/code) Final Project
Group members:
- Caitlin Carpenter
- Nick Danis
- Jonathan Viereck

## Description
Every regular NYT Crossword fan knows that Monday is the easiest and the end of the week is most difficult. Given an arbitrary crossword puzzle, can we predict what day it was from?

## Feature Selection
We scraped 27 years of NYT Crossword puzzle data (Jan 1, 1994-Jan 1, 2021, essentially the entire Will Shortz era to date), collecting clue/answer text as well as other puzzle metadata such as puzzle size, number of black blocks, and authors, from [https://www.xwordinfo.com/](xwordinfo.com). All totaled, the data set contains 815332 hint/answer pairs. Neither the scraper nor the retrieved dataset are stored in this repository. 

The hint/answer pairs and puzzle metadata were used to construct features for the classification models from the set of roughly 10k different crossword puzzles. Puzzle features considered were

- **Puzzle grid size**
- **Block density**: Percentage of the puzzle grid consisting of black blocks.
- **Average hint/answer length**
- **Number of hints**
- **Number of One-Word Hints**
- **Number of hints ending in a question mark**
- **Number of clues containing a proper noun**

Additionally we computed 
- **Answer Rarity**: The number of times answers in a puzzle have appeared in other puzzles across the data set

- **Perplexity Outliers**: A character bigram language model is trained on all puzzle answers using [nltk](http://www.nltk.org/)'s [Maximum Likelihood Estimation model](https://www.nltk.org/api/nltk.lm.html). [Perplexity](https://en.wikipedia.org/wiki/Perplexity) is calculated for each answer, and the number of **perplexity outliers** (those whose perplexity score is $$> 1.5*IQR$$) are counted for each puzzle. The intuition here is that answers that are more rare or obscure should have a higher perplexity score, and that certain days of the week might have on average more ansers of this type than others. 

- **Bag of Words** and **Term frequency - Inverse document frequency (tf-idf)**: Each puzzle was considered as a documents by joining all its hints into a single string, and were represented with Bag-of-words and tf-idf vectors using the `sklearn` functions `CountVectorizer()` and `TfidfVectorizer()`.

## Models

1. (ND/CC) Using the features computed from puzzle metadata, cross-validation was used to determine the most relavent subset of features for fitting K nearest neighbors, decision tree, and random forest models.

2. (JV) Using the Bag of Words and tfidf vector representations, we considered linear SVM, random forest, boosted decision tree, and feed-forward neural network models to classify the data.

## Results

Testing accuracies for classification on metadata can be compared to the bag-of-words and tf-idf classification models. In both cases testing accuracies were around 50%, compared to random guessing of about 15%

Metadata            |  Bag of Words & tf-idf
:-------------------------:|:-------------------------:
![meta_accs](plots/metadata_accs.png)  |  ![accs](plots/bow_tfidf_acc.png)

Out of the models tested, the linear SVM model on tf-idf vectors achieved the highest accuracy of 52.5%. 

![svm_tfidf](plots/tfidf_SVM_cmat.png)

The confusion matrices for every model tested are all qualitatively similar to the one above. Weekly puzzles can be broken up into three  irreducible categories: (1) Sunday was by far the easiest to classify, which is unsurprising given that Sunday puzzles are larger and contain more information than puzzles from other days of the week (2) Friday and Saturday were difficult to separate from each other, but easy to separate from (3) Monday, Tuesday, Wednesday, Thursday, which were also difficult to separate from each other. 

## Next steps

- Improve the classification of the individual days based on more sophisticated language models.
- It would be interesting to find out if the crossword puzzles from other major newspapers follow the same trends. Lastly, 
- Include a parser for the `.puz` file format 
