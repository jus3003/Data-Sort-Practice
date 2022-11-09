

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
    print("A list created from a slice starting with the 4th element and includes every third element after that:", sliced_list) 

tupleizer("integers.txt")


    
