# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 00:28:06 2020

@author: User
"""



import re

        

def hapax():
    myfile=open('bambi.txt', 'r', endcoding='utf8')
    all_word=re.findall('\w+', f.read().lower())
    dict={}
    
    for word in all_words:
        dict[word] +=1
    for  word in dict:
        if dict[word] ==1:
            print(word)
             
        

    
        

if __name__ == "__main__":
    
    
    hapax()
    
    

