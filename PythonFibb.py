# -*- coding: utf-8 -*-
"""
@title: Fibonacci Sequence
@function: Enter a number and have the program generate the 
Fibonacci sequence to that number or to the Nth number.
@author: Zhilin
"""
def fibb(n):
    '''
    generate n-th Fibonacci Sequence number using recursion
    using yield function can greatly decrease the running time
    '''
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b, a+b

def upper(N):
    '''
    generate and print the Fibbonacci Sequence up to 
    the input number
    '''
    i=1
    while True:
        out= list(fibb(i))[i-1]
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
        for i in fibb(num):
            print(i, end=' ')
    else:
        upper(num)

main()
