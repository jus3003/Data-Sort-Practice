# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:07:20 2022

@author: jusxp
"""

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
    
myCalculator()