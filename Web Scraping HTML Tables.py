# -*- coding: utf-8 -*-
"""Created on Mon Jun  3 23:29:27 2019
@author: fabio
source : https://github.com/snazrul1/PyRevolution/blob/master/Puzzles/PokeScraper.ipynb 
"""

import requests, six
import lxml.html as lh
from itertools import cycle, islice
from matplotlib import colors
import pandas as pd
import matplotlib.pyplot as plt

#-------------------------------------------------------------------
#Scrape Table Cells
#-------------------------------------------------------------------

url='http://pokemondb.net/pokedex/all'
#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

#Check the length of the first 12 rows
[len(T) for T in tr_elements[:12]]

#-------------------------------------------------------------------
#Parse Table Header
#-------------------------------------------------------------------

tr_elements = doc.xpath('//tr')
#Create empty list
col=[]
i=0
#For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    print (i,name)
    col.append((name,[]))

#-------------------------------------------------------------------
#Creating Pandas DataFrame / Each header is appended to a tuple along with an empty list.
#-------------------------------------------------------------------
    
#Since out first row is the header, data is stored on the second row onwards
for j in range(1,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]
    
    #If row is not of size 10, the //tr data is not from our table 
    if len(T)!=10:
        break
    
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content() 
        #Check if row is empty
        if i>0:
        #Convert any numerical value to integers
            try:
                data=int(data)
            except:
                pass
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1
        
[len(C) for (title,C) in col]

Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)

#-------------------------------------------------------------------
#Clean up data 
#-------------------------------------------------------------------
    

def str_bracket(word):
    '''Add brackets around second term'''
    list = [x for x in word]
    for char_ind in range(1, len(list)):
        if list[char_ind].isupper():
            list[char_ind] = ' ' + list[char_ind]
    fin_list = ''.join(list).split(' ')
    length = len(fin_list)
    if length>1:
        fin_list.insert(1,'(')
        fin_list.append(')')
    return ' '.join(fin_list)

    
def str_break(word):
    '''Break strings at upper case'''
    list = [x for x in word]
    for char_ind in range(1, len(list)):
        if list[char_ind].isupper():
            list[char_ind] = ' ' + list[char_ind]
    fin_list = ''.join(list).split(' ')
    return fin_list

df['Name']=df['Name'].apply(str_bracket)
df['Type']=df['Type'].apply(str_break)
#print(df.head(6))

#-------------------------------------------------------------------
#Storing Data
#-------------------------------------------------------------------

#write
df.to_json('PokemonData.json')
#read to confirm 
df = pd.read_json('PokemonData.json')
df=df.set_index(['#'])

#-------------------------------------------------------------------
#Stats1- max e min
#-------------------------------------------------------------------
                
                 
def max_stats(df, col_list):
    '''Get Pokemon highest value of the column in the Data Frame'''
    message = ''
    for col in col_list:
        stat = df[col].max()
        name = df[df[col]==df[col].max()]['Name'].values[0]
        message += name+' has the greatest '+col+' of '+str(stat)+'.\n'
    return message

def min_stats(df, col_list):
    '''Get Pokemon lowest value of the column in the Data Frame'''
    message = ''
    for col in col_list:
        stat = df[col].min()
        name = df[df[col]==df[col].min()]['Name'].values[0]
        message += name+' has the worst '+col+' of '+str(stat)+'.\n'
    return message                 

stats=['Attack', 'Defense','HP', 'Sp. Atk','Sp. Def','Speed','Total']
print (max_stats(df, stats))
print (min_stats(df, stats))

#-------------------------------------------------------------------
#Stats2- scatter plot e correlations 
#-------------------------------------------------------------------

from pandas.tools.plotting import scatter_matrix
scatter_matrix(df[stats[:-1]], alpha=0.2, figsize=(10, 10), diagonal='kde')


#-------------------------------------------------------------------
#Stats3- Creating new Data Frame where the Type values are separated from the list
#-------------------------------------------------------------------

#Creating new Data Frame where the Type values are separated from the list
newDict={}
stats_col=["#","Name","Total","HP","Attack","Defense","Sp. Atk","Sp. Def","Speed"]

#Collecting the list of Type for each Pokemon
Dict['Type']=df['Type'].values

#Creating an empty list for each key (column)
for col in stats_col:
    newDict[col]=[]
    newDict['Type']=[]

#Populating each the dictionary value (empty list) with data 
for row in range(len(Dict['#'])):
    for t in Dict['Type'][row]:
        for col in stats_col:
            #Append all columns except Type to the new dictionary
            newDict[col].append(Dict[col][row])
        #Appending the Type separately for each Pokemon  in the new dictionary
        newDict['Type'].append(t)
        
#Convert dictionary to a Data Frame
new_df = pd.DataFrame(newDict)
#print(new_df.head(10))

types=new_df['Type'].unique()
print (types)

#Colours to cycle through when plotting the hbar graph
my_colors = list(six.iteritems(colors.cnames))
my_colors = list(islice(cycle(my_colors), None, len(new_df)))

def barh_stats():
    '''Plot hbar of mean and std. of each attribute of Pokemon Type'''
    i=0
    plt.figure(figsize=(15,5))
    plt.suptitle('Statistics', fontsize=15)
        
    #Cycle through each pokemon Type
    for t in types:
        
        #Iterate i value to change colour to my_colors[i]
        i+=1   
        
        #Plotting Mean
        plt.subplot(121)
        plt.title('Mean')
        new_df[new_df['Type']==t].mean().plot(kind='barh', color=my_colors[i])
        
        #Plotting Standard Deviation
        plt.subplot(122)
        plt.title('Standard Deviation')
        new_df[new_df['Type']==t].std().plot(kind='barh', color=my_colors[i])
    
    #Add list of Pokemon Type to legend
    plt.legend(types,bbox_to_anchor=(1.3, 1.1))
    
barh_stats()
