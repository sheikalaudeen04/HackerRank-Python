def alpnum(s):
    for char in s:
        if char.isalnum():
            return True
    return False        
def alpha(s):
    for char in s:
        if char.isalpha():
            return True
    return False        

def digit(s):
    for char in s:
        if char.isdigit():
            return True
    return False        

def lower(s):
    for char in s:
        if char.islower():
            return True
    return False 
    
def upper(s):
    for char in s:
        if char.isupper():
            return True
    return False        
    
if __name__ == '__main__':
    s = input()
    print(alpnum(s))
    print(alpha(s))
    print(digit(s))
    print(lower(s))
    print(upper(s))
    