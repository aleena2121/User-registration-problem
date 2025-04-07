import re

first_name_check = None
while first_name_check == None:
    first_name = input("\nEnter First Name: ")
    first_name_check = re.fullmatch(r"\b[A-Z][a-z]{2,}",first_name)
    if first_name_check == None:
            print("Name should start with capital letter and have atleast 3 letters!!")
    