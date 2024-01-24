#description
#create a function that takes an integer as an argument and return "even" for even number or "odd" for odd numbers

#write function that takes in integer
#evaluate weather or not that int is even or odd
# --- most likely need to use if statement with % to eval even
#return the string "even" or "odd" depending on the int

def even_or_odd(num):
    
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_or_odd(10))