import random
import string
from faker import Faker

#
# def generate_password(password_len: int = 10) -> str:
#     if not isinstance(password_len, int):
#         raise TypeError('Invalid Type...')
#
#     choices = string.ascii_letters + string.digits + '#$%^'
#     result = ''
#
#     for _ in range(password_len):
#         result += random.choice(choices)
#
#     return result


def read_requirements_txt():
    with open("requirements.txt", "r") as txt_file:
        return txt_file.read()

def making_users(users_numb=10):
    fake = Faker()
    user = ''

    for _ in range(users_numb):
        user += fake.name() + " " + fake.email() + " "
    return user