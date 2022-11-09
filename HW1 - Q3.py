# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 01:01:34 2022

@author: jusxp
"""

def wordCloud(filename):

    import matplotlib as mp
    import pandas as pd
    from wordcloud import WordCloud, STOPWORDS
    import matplotlib.pyplot as plt
    from PIL import Image
    
    file = open(filename,"r")
    
    title_list = []
    
    
    #Part A: Parse File for List Titles
    
    for line in file:
        line_parse = line.replace(" ", "--", 1).replace("\n", "--").split("--")
        #print(line_parse)
        
        if line_parse[0].isnumeric():
            line_parse.pop(0)
            line_parse.pop(-2)

            line_parse = list(filter(None, line_parse))
            title_list.append(line_parse)
            
    stripped_title_list = [sublist[0].split() for sublist in title_list]
            
    #print("")
    #print(stripped_title_list)
    
    #Part B: Create String for WordCloud Input
    
    string_list = []
    
    #Part B1: Flat List
    string_list = [item for sublist in stripped_title_list for item in sublist]
    #print(string_list)
    
    #Part B2: Convert List to String
    string = (" ").join(string_list).lower()
    #print(string)
    
    #Part C: Create Standard Workcloud
    wordcloud = WordCloud(collocations = False, relative_scaling = 0.5, stopwords = ["dontremoveconnectingwords"], max_words = 1000000, height = 250, background_color = "white").generate(string)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    
    #Part D: Create Workcloud with Ommitted Words
    stop_words = [ 'a', 'an', 'the', "for", "and", 'nor', 'but', "or", 'yet', 'so', 'at', 'around', 'by', 'after', 'along', "for", 'from', 'of', 'on', 'to', 'with', 'without' ]
    wordcloud_2 = WordCloud(collocations = False, relative_scaling = 0.5, stopwords = stop_words, max_words = 1000000, height = 250, background_color = "white").generate(string)
    plt.imshow(wordcloud_2, interpolation = 'bilinear')
    plt.axis("off")
    plt.show()

wordCloud("scifibookfavorites.txt")
