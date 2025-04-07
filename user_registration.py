import re

def check_name(name):
    """
    This function checks if the given name is starting with a capital letter and has a minimum of 3 letters
    """
    return re.fullmatch(r"[A-Z][a-z]{2,}", name)

def check_email(email):
    """
    This function checks if the given mail id is valid or not
    """
    return re.fullmatch(r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$",email)

def check_phone_number(number):
    """
    This function checks if the given number follows this format :- Country code follow by space and 10 digit number
    """
    return re.fullmatch(r"\d{2}\s\d{10}",number)

def check_password(password):
    """
    This function checks if the password follows the specified rules
    Rule 1 : should have minimum 8 characters
    Rule 2 : Should have atleast one upper case
    Rule 3 : should have atleast 1 numeric value
    Rule 4 : should have atleast 1 special character
    """
    return re.fullmatch(r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()]).{8,}$",password)

first_name = input("\nEnter First Name: ")
while check_name(first_name) is None:
    print("\nName should start with a capital letter and have at least 3 letters!")
    first_name = input("\nEnter First Name: ")

last_name = input("\nEnter Last Name: ")
while check_name(last_name) is None:
    print("\nName should start with a capital letter and have at least 3 letters!")
    first_name = input("\nEnter Last Name: ")

email_id = input("\nEnter your EmailID: ")
while check_email(email_id) is None:
    print("\nEnter Valid EmailID!")
    first_name = input("\nEnter your EmailID: ")

phone_number = input("\nEnter your phone number: ")
while check_phone_number(phone_number) is None:
    print("\nEnter Valid phone number!!")
    phone_number = input("\nEnter your phone number: ")
    
password = input("\nEnter your password: ")
while check_password(password) is None:
    print("\nEnter Valid password!!")
    password = input("\nEnter your password: ")