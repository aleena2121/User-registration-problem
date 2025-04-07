import re

is_first_name_valid = None
while is_first_name_valid == None:
    first_name = input("\nEnter First Name: ")
    is_first_name_valid = re.fullmatch(r"\b[A-Z][a-z]{2,}",first_name)
    if is_first_name_valid == None:
            print("Name should start with capital letter and have atleast 3 letters!!")


is_last_name_valid = None
while is_last_name_valid == None:
    last_name = input("\nEnter Last Name: ")
    is_last_name_valid = re.fullmatch(r"\b[A-Z][a-z]{2,}",last_name)
    if is_last_name_valid == None:
            print("Name should start with capital letter and have atleast 3 letters!!")
    