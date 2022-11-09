# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 13:34:37 2022

@author: jusxp
"""

def scifiAuthors(filename):
  
    #Part A: Remove no nominations, Remove book titles
    #file = open("scifibookfavoritestest.txt","r")
    file = open(filename,"r")
    
    nomination_list = []
    for line in file:
        #line_parse = line.replace(" ", ",", 1).replace("--",",").replace("\n", ",").split(",")
        line_parse = line.replace(" ", "--", 1).replace("\n", "--").split("--")
        #print(line_parse)
        if line_parse[0].isnumeric():
            line_parse.pop(1)
            line_parse.pop(-1)
            line_parse[0] = int(line_parse[0])
            line_parse[-1] = line_parse[-1].strip()
            nomination_list.append(line_parse)
            
    #print(nomination_list)
    
    #Part B: Count number of books and nominations for each author -> input into dictionary
    
    nomination_dict = {}
    books_dict = {}
    
    # for elem in nomination_list:
    #     if nomination_dict[elem[1]] is None:
    #         nomination_dict[elem[1]] = [elem[0]]
    #     else: 
    #         nomination_dict[elem[1]] += [elem[0]]
    
    for elem in nomination_list:
        if elem[1] in nomination_dict:
            nomination_dict[elem[1]] = nomination_dict[elem[1]]+elem[0]
            books_dict[elem[1]] = books_dict[elem[1]] + 1 
        else:
            nomination_dict[elem[1]] = elem[0]
            books_dict[elem[1]] = 1
                     
    #print(nomination_dict)
    #print(books_dict)
    
    
    #Part C: Sort for Author with most Nominations, Sort equal nominations by alphabetical last name
    
    
    sorted_author = sorted(nomination_dict.items(), key = lambda item: (-item[1], item[0]), reverse = False)
        #print(sorted(nomination_dict.items())   
    
    sorted_author_dict = {}
    for key, value in sorted_author:
        sorted_author_dict[key] = value
    #print(sorted_author_dict)
    
    
    
    #Part D: Print Outputs
    
    for key in sorted_author_dict: 
        
        if sorted_author_dict[key] > 1:
            if books_dict[key] > 1:
                print(key.split(',')[0],":", books_dict[key], "books with", sorted_author_dict[key], "total nominations" )
            elif books_dict[key] <= 1:
                print(key.split(',')[0], ":", books_dict[key], "book with", sorted_author_dict[key], "total nominations" )
        else:
            print(key.split(',')[0], ":", books_dict[key], "book with", sorted_author_dict[key], "total nomination" )
            
    
scifiAuthors("scifibookfavorites.txt")   
    
    
    
    
    
