import random
import string
import sys
import logging



logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {message}",
    style='{',
    filename='%slog' % __file__[:-2],
    filemode='a'
)

def passwordgen():
    num = int(input("password length "))

    source = string.ascii_letters + string.digits + '!@#$%^&*()_@'
    result_str = ''.join((random.choice(source) for i in range(num)))
    print(result_str)
    logging.debug(result_str)
    question = input("quit ? ")
    if question == "n":
        passwordgen()
    else:
          sys.exit()
passwordgen()