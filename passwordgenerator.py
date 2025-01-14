import random   
import string

def generating_pass(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits  
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    password = ""
    meetscriteria = False
    hasnumber= False
    hasspecial= False
    
    while not meetscriteria or len(password) < min_length:
        newchar = random.choice(characters)  
        password += newchar
        
        if newchar in digits:
            hasnumber = True  
        elif newchar in special:
            hasspecial = True

        meetscriteria = True
        if numbers:
            meetscriteria = hasnumber
        if special_characters:
            meetscriteria = meetscriteria and hasspecial
    return password
    
min_length = int(input('Enter the minimum length:'))
hasnumber = input('Do you want to have numbers (y/n)?').lower() == 'y'
hasspecial = input('Do you want to have special characters (y/n)?').lower() == 'y'
password = generating_pass(min_length, hasnumber, hasspecial)
print('The Generated Password is:', password)