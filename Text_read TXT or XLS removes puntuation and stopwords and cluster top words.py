# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 22:52:25 2019
"read txt or XLS removes puntuation and stopwords and cluster top words"
Imports txt removes puntuation and stopwords from standard and custom lists. cluster top words.

USEFUL PARTS : 
> imports TXT as string
> imports XLS as dataform
> converts lista to dataframe
> converts dataframe to string
> Stopwords_ENG2 = from txt to list 
> removes puntuation 
> removes stopwords from string 
    split_it_noStopwords= [ x for x in split_it if not x in Stopwords_ENG ] 
> removes stopwords from dataform
    df['ISSUE'] = df['ISSUE'].apply(lambda x: ' '.join([word for word in x.split() if word not in (Stopwords_ITA)]))
> cluster top words
> most_occur_df = convert list to dataframe 
> English standard stopwords library 

    RUN ONCE 
    #import nltk
    #nltk.download('stopwords')
    
    #from nltk.corpus import stopwords
    
@author: fabio
"""

import string
from string import punctuation
from collections import Counter
from nltk.corpus import stopwords
# 4 tipi di stopwords: Stopwords_ENG downloadato once,Stopwords_ENG2 e ITA un file txt,Stopwords_ITA2 una lista in procedura 

Stopwords_ENG = stopwords.words('english')
Stopwords_ENG2= np.genfromtxt('Text_Stop_words_ENG_part2.txt', delimiter=',', dtype=str)
Stopwords_ENG2 = Stopwords_ENG2[:].tolist()
Stopwords_ITA2 = ["ISSUE","Amazon"]
Stopwords_ITA= np.genfromtxt('Text_NLP_ITA_Stopwords.txt', delimiter=',', dtype=str)
Stopwords_ITA = Stopwords_ITA[:].tolist()

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

##SCENARIO1 - XLS 
#file = "Text_lista.xlsx"
#df = pd.read_excel(file)
#data_set = df.to_string()

##SCENARIO2 - TXT
file = open('Text_dracula.txt')
data_set= file.read()

data_set = strip_punctuation(data_set) #elimina punteggiatura
split_it = data_set.split()  # split() returns list of all the words in the string 
split_it_noStopwords= [ x for x in split_it if not x in Stopwords_ENG ] # Elimina stopwords1
split_it_noStopwords= [ x for x in split_it_noStopwords if not x in Stopwords_ENG2 ] # Elimina stopwords1
split_it_noStopwords= [ x for x in split_it_noStopwords if not x in Stopwords_ITA ] # Elimina stopwords1
split_it_noStopwords= [ x for x in split_it_noStopwords if not x in Stopwords_ITA2 ] # Elimina stopwords1
  
Counter = Counter(split_it_noStopwords) # Pass the split_it list to instance of Counter class. 
most_occur = Counter.most_common(40) # most_common() produces k frequently encountered input values and their respective counts. 

most_occur_df = pd.DataFrame(most_occur, columns = ['word' , 'Count'])  #converte lista in dataframe

print(most_occur_df) 
most_occur_df.plot.bar(x='word',y='Count')






