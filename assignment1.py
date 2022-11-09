#!/usr/bin/bash python3
"""
Assignment1 ME369P/ME396P/ES122
Name: <Justin Lam>
EID : <JHL2965>
Fill in the 4 functions below
"""

def tupleizer(filename):
    #Open file and convert from txt to list of integers
    file = open(filename, "r")
    #tuples_unfiltered = []
    tuples = []
    for line in file:
        line_strip = line.strip()  
        tuples.append(line_strip)    
    file.close()
    #print(type(tuples[1]))
    tuples = [a for a in tuples if a.isnumeric()]
    tuples = [int(x) for x in tuples]
    #print(type(tuples[1]))
    
    print("The difference between the largest and smallest value:", max(tuples) - min(tuples))
    print("The number of items in the tuple:", len(tuples)) 
    
    #even numbers in tuples
    even_count = 0
    for i in range(len(tuples)):
        if tuples[i]%2 == 0:
            even_count += 1 
    print("The number of even integers in the tuple:", even_count) 
    
    print("The sum of the values in the tuple:", sum(tuples))
    
    average = round(sum(tuples)/len(tuples), 2)
    #print(type(average))
    print("The average of the values:", average)
    
    #check for prime numbers
    not_prime_count = 0 
    
    for i in range (len(tuples)):
        if (tuples[i]>1):   
            for x in range(2,tuples[i]):
                if (tuples[i] % x) == 0:
                    not_prime_count +=1
                    #print(tuples[i], x)
                    break
        else: 
            not_prime_count += 1
    print("The number of prime numbers in the tuple:", len(tuples) - not_prime_count)
    
    #Tuple -> Set
    s = set(tuples)
    print("The number of items if the tuple is converted to a set:", len(s))
    
    sliced_list = tuples[3::3]
    sliced_list = str(sliced_list).replace(',', '')
    print("A list created from a slice starting with the 4th element and includes every third element after that:", sliced_list)


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

def myCalculator():
    
    operation = str()
    operation = input("Enter operation: ")
    
    while operation != 'q':
        if operation == 'q':
            break
        else:
            first_num = input("Enter First Number: ")
            if first_num == "":
                first_num = float(0)
            else:
                first_num = float(first_num)
            
            second_num = input("Enter Second Number: ")
            if second_num == "":
                second_num = float(0)
            else:
                second_num = float(second_num)
    
            print("")
            
            if operation == '+':
                add = first_num + second_num
                print(round(add, 1), end = "")
            elif operation == '/':
                div = first_num / second_num
                print(round(div, 1), end = "")
            elif operation == '-':
                subtract = first_num - second_num
                print(round(subtract, 1), end = "")
            elif operation == '^':
                exp = first_num**second_num
                print(round(exp, 1), end = "")
            else: 
                print("Operator Not Valid, Enter One of the Following: +, /, -, ^")
                
            print("")
    
        operation = input("Enter operation: ")


if __name__ == '__main__':
    tupleizer("integers.txt")
    scifiAuthors("scifibookfavorites.txt")
    wordCloud("scifibookfavorites.txt")
    myCalculator()
    
