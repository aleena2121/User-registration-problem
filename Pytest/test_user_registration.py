import random
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import user_registration

import pytest
from faker import Faker
from loguru import logger

logger.add("fails.log",level = "ERROR")

fake = Faker()

def generate_valid_test_cases():
    """
    This fucntion generates valid test cases
    """
    return (
        True,
        fake.first_name(),
        fake.last_name(),
        fake.email(),
        f"{fake.random_int(min=10, max=99)} {fake.msisdn()[0:10]}",
        fake.password()
    )

def generate_invalid_test_cases():
    """
    This function generates invlalid test cases
    """
    variant = random.randint(1, 4)

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone = f"{fake.random_int(min=10, max=99)} {fake.msisdn()[:10]}"
    password = fake.password(
        length=random.randint(4, 8),
        special_chars=random.choice([True, False]),
        digits=random.choice([True, False]),
        upper_case=random.choice([True, False]),
    )

    if variant == 1:  
        first_name = fake.first_name().lower()

    elif variant == 2:  
        email = email.replace("@", "")  

    elif variant == 3: 
        phone = fake.msisdn()[:10]  

    elif variant == 4: 
        phone = f"{fake.random_int(min=10, max=99)} {fake.msisdn()[:9]}"

    return (False, first_name, last_name, email, phone, password)

test_cases = [generate_valid_test_cases() for i in range(1000)] + [generate_invalid_test_cases() for i in range(1000)]
    
@pytest.mark.parametrize("is_valid, first_name, last_name, email_id, phone_number, password", test_cases
)
def test_user_validations(is_valid,first_name, last_name, email_id, phone_number, password):
    result = (
         user_registration.check_name(first_name) is not None and
        user_registration.check_name(last_name) is not None and
        user_registration.check_email(email_id) is not None and
        user_registration.check_phone_number(phone_number) is not None and
        user_registration.check_password(password) is not None
    )
    if result != is_valid:
        logger.error(f"{(is_valid,first_name, last_name, email_id, phone_number, password)}")
    assert result == is_valid