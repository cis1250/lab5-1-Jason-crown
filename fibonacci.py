#!/usr/bin/env python3
# This loops till it gets the input, is a # & #>0
def get_terms():
    while True:
        n = input("How many Fibonacci terms? ")
        if n.isdigit() and int(n) > 0:
            return int(n)
        print("Please enter a positive number.")

# This makes the sequence with the input 
def make_fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib

# This shows the sequence with the input
def show_fib(fib):
    print("Fibonacci sequence:")
    print(*fib, sep=", ") # this is just to make it look nicer (unpacking then adding ",")
  
# This function feeds the terms to one another
def main():
    n = get_terms()
    seq = make_fib(n)
    show_fib(seq)

main() # Function call
# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
