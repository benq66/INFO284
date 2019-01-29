import pandas as pd
import nltk
from nltk.corpus import stopwords

from nltk import word_tokenize
import numpy as np
from scipy import sparse
from IPython.display import display
import matplotlib.pyplot as plt

pd.options.display.max_colwidth = 1000
# train = pd.read_csv('C:/Users/And/Desktop/stuff/INFO284/oblig 1 og 2/dataset/train.csv')

# words = set(nltk.corpus.words.words())
# print(train.shape)
# train = train.join(w for w in nltk.word_tokenize(train)
#                    if w.lower() in words or not w.isalpha())
# print(train.shape)

# train.head(10)
# print(train.shape)

# for word in text:
#     if word.contains("[0-9]", regex=True, na=False):
#         word = ""
#
#
# train['text'] = text

# print(train.shape)
# text = train['text']
# filter = text.str.contains("Trump", na=False)
# train['text'] = filter
# print(train.shape)

# def remove_text(row):
#     return True

# for index, row in train.head().iterrows():
#     filter.append(remove_text(row['text']))
#     train.dropc()

# data_frame_train = pd.DataFrame(train)

# plt.show(data_frame_train.head(10))
# display(data_frame_train.head(10))
# dataframe = pd.DataFrame(train)
# display(dataframe)

train = pd.read_csv('C:/Users/And/Desktop/stuff/INFO284/oblig 1 og 2/dataset/train.csv')
# print(train['title'][:20])
train = train.sample(frac=1, random_state=0)
# train.head()
# train_dataframe = pd.DataFrame(train)
# train_dataframe.head()

# print(type(train['title']))

train['Length'] = [len(str(title)) for title in train['title']]
# train.head()

# print(train['Length'].describe())

notfake_text = ' '.join(str(word).lower() for word in train['title'][train['label'] == 1])
# notreal_text = ' '.join(train[train['label'] == 0]['title'])

notfake_text_words = nltk.tokenize.word_tokenize(notfake_text)

print(notfake_text_words[:10], '\n {}' .format(len(notfake_text_words)))

notfake_text_words = [word for word in nltk.tokenize.word_tokenize(notfake_text)
                      if word not in stopwords.words('english') and len(word) > 3]

print(notfake_text_words, '\n {}' .format(len(notfake_text_words)))
