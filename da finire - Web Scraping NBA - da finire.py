# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 00:30:42 2019
@author: fabio
"""

#import pandas as pd
#import html5lib
#url = 'https://www.basketball-reference.com/leagues/NBA_2019_per_game.html'
#dfs = pd.read_html(url)
#df = pd.concat(dfs)
#df

def max_stats(df, col_list):
    dfz=df.copy()
#    dfz.columns = dfz.iloc[0]
#    dfz= dfz[1:]
    message = ''
    for col in col_list:
        stat = dfz[col].max()
        name = dfz[dfz[col]==dfz[col].max()]['Player'].values[0]
        message += name+' has the greatest '+col+' of '+str(stat)+'.\n'
    return message

def min_stats(df, col_list):
    message = ''
    for col in col_list:
        stat = df[col].min()
        name = df[df[col]==df[col].min()]['Player'].values[0]
        message += name+' has the worst '+col+' of '+str(stat)+'.\n'
    return message                 


#stats=list(df)
#stats. remove('Player')
#stats. remove('Tm')
#stats. remove('Pos')

stats=('Age', 'G', 'GS', 'MP','BLK')
print(list(df))

print (max_stats(df, stats))
print (min_stats(df, stats))


#problema 1 . 
#non posso fare il MAX perche considera la header come valore MAX . 
#non posso eliminare header perche poi non so chiamare le colonne

#ATTENZIONE A COME SI COPIA UN DF .. SE FACCIO DF=DFZ OGNI MODIFICA SI RIFLETTE SU ENTRAMBI 
#USARE dfz=df.copy()

#
#print(df.Age.unique())
#dfz=df.copy()
#dfz.columns = dfz.iloc[0]
#dfz= dfz[1:]
#print(df.shape)
#print(dfz.shape)

#non posso convertire in numerico perche la header  lo impedisce 

#df = df.infer_objects() 
#print(df.dtypes)
#df[['Age', 'FGA']] = df[['Age', 'FGA']].apply(pd.to_numeric) 
#print(df.dtypes) 



 