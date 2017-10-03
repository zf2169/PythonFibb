# -*- coding: utf-8 -*-
"""
@title: Fibonacci Sequence
@function: Enter a number and have the program generate the 
Fibonacci sequence to that number or to the Nth number.
@author: Zhilin
"""
def fibb(n):
    '''
    generate the n-th Fibonacci number using recursion
    '''
    if n==1 or n==2:
        return(1)
    else:
        return(fibb(n-1)+fibb(n-2))

def upper(N):
    '''
    generate and print the Fibbonacci Sequence up to 
    the input number
    '''
    i=1
    while True:
        out= fibb(i)
        if out<N:
            i += 1
            print(out, end=' ')
        else:
            break

def style():
    '''
    input a choice 
    '''
    while True:
        try:
            choice= int(input('You want to generate:\n 1.Nth number.\n 2.to the number:'))
        except ValueError:
            print('Please input a valid number.')
            continue
        
        if choice not in [1,2]:
            print('Please choose 1 or 2.')
            continue
        else:
            return(choice)
        
def main():
    choice= style()
    while True:
        try:
            num= int(input('Please input your number:'))
        except ValueError:
            print('Please input a valid number.')
            continue
        else:
            break
        
    if choice==1:
        for i in range(1,num+1):
            print(fibb(i), end=' ')
    else:
        upper(num)

main()

