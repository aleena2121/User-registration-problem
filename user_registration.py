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
    