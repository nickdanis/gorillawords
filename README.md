# Predicting difficulty in NY Times Crossword puzzles

## [Erdős Code May 2021 Bootcamp](https://www.erdosinstitute.org/code) Final Project
Group members:
- Caitlin Carpenter
- Nick Danis
- Jonathan Viereck

## Description
Every regular NYT Crossword fan knows that Monday is the easiest and the end of the week is most difficult. We extract a number of features from the data based and train several classifiers in an attempt to predict the given day of the week for a given puzzle, as a proxy for difficulty (or other metrics). 

## Feature Selection
We scraped 27 years of NYT Crossword puzzle data (Jan 1, 1994-Jan 1, 2021, essentially the entire Will Shortz era to date), collecting clue/answer text as well as other puzzle metadata such as puzzle size, number of black blocks, and authors, from [https://www.xwordinfo.com/](xwordinfo.com). All totaled, the data set contains 815332 hint/answer pairs. Neither the scraper nor the retrieved dataset are stored in this repository.

Features considered for the classification models were
- **Average answer length**
- **Puzzle size**
- **Block density**: Percentage of the puzzle grid consisting of black blocks.
- **Puzzle author**

Additionally we computed 
- **Answer Rarity**: The number of times answers in a puzzle have appeared in other puzzles across the data set

- **Perplexity Outliers**: A character bigram language model is trained on all puzzle answers using [nltk](http://www.nltk.org/)'s [Maximum Likelihood Estimation model](https://www.nltk.org/api/nltk.lm.html). [Perplexity](https://en.wikipedia.org/wiki/Perplexity) is calculated for each answer, and the number of **perplexity outliers** (those whose perplexity score is $> 1.5*IQR$) are counted for each puzzle. The intuition here is that answers that are more rare or obscure should have a higher perplexity score, and that certain days of the week might have on average more ansers of this type than others. 

- **Bag of Words** and **Term frequency - Inverse document frequency** (tf-idf)

## Models

ND/CC For the features ... we considered KNN, Random Forest ..

JV for the Bag of Words and tfidf models, we considered linear SVM, random forest, boosted decision tree, and feed-forward neural network models. The Linear SVM model achieved the highest accuracy of 52%.

## Results

Sunday was by far the easiest for the classifiers, with a true positive rate consistently above 90%. Friday and Saturday were difficult to separate from each other, but easy to separate from Monday, Tuesday, Wednesday, Thursday, which were also difficult to separate from each other.

## Code

TBA


