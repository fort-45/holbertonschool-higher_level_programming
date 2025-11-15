#!/usr/bin/python3
def print_last_digit(number):
   last = abs(number) % 10
   print(last, end="")
    
print_last_digit(6)    
print_last_digit(5698)    
print_last_digit(-3456)
