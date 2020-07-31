# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 02:28:32 2020

@author: Ankit
"""
import pandas as pd

file = open('messy_data.txt')
content= file.read()
file.close()
####################################################################################
lines = content.split("\n")     #splitting text data with \n. And storing the resulting list of lines from .txt in a new object.
####################################################################################

#observation : messy_data has no common separator and non-uniform patterns.
#idea : to add more noise data to the messy_data to make it uniform pattern. And splitting it further to perform cleaning actions.

m=lines.copy()  #creating a dummy data to work upon.
m.pop(2)        #3rd row of the data is not needed.

for i in range(len(m)):
    m[i]=m[i].replace('  ','**')    #adding ** in place of spaces to make the pattern of noisy data common.

for i in range(len(m)):
    m[i]=m[i].split('*')            #now treating * to be common separator, we will split the individual lines.
    m[i]=list(filter(lambda x : x != '',m[i]))    #filtering only the data excluding any additional strings of space created as a result of above splitting.
    m[i]=list(filter(lambda x : x != ' ',m[i]))    #filtering only the data excluding any additional strings spaces created as a result of above splitting.
    for j in range(len(m[i])):
        m[i][j]=m[i][j].strip()    #removing white spaces from desired elements of data in the list.

#additional operations done to bring the data in nicest form before creating a dataframe out of it.
n=m.pop(1)
n.reverse()
n.append('')
n.reverse()
m[0]= [i + j for i, j in zip(m[0], n)] #concatenating the contents of row 0 and row 1 element-wise.
m.pop(-1)

data=pd.DataFrame(m,columns=m[0])      #converting the list of lists into a data frame and assigning column name as first list from the list of lists.
data.drop(data.index[0],inplace=True)  # dropping the first list from the list of lists.
data.to_csv('cleaned.csv')             #saving the .csv file on local machine.