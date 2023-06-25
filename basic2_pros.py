number = 234234

def palindrome_check(n):
    other = n 
    reverse_number = 0 
    while other > 0: 
        remainder = reverse_number % 10
        reverse_number = (reverse_number*10) + remainder
        other = other//10
    
    if reverse_number == n :
        print("true")
    else:
        print("fa")
    
palindrome_check(123222)