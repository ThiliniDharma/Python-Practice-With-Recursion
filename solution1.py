# Write code for algorithm 1 below
#Write a program that takes a positive number as an argument and prints the numbers from n to zero.

def print_positive_numbers(n):
    if(n >= 0):
        print(n)
        if( n!= 0):
           print_positive_numbers(n-1)

print_positive_numbers(5)
