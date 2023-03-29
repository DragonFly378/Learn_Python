# modules can install using pip package manager

# import datetime
from datetime import date

# pip modules
from camelcase import CamelCase

# Custom Modules using validator.py
# import validator 
#   or we can write like this
from validator import validate_email

# today = datetime.date.today()
today = date.today()

# inisiasi p menjadi objek
p = CamelCase()

# print(p.hump("halo semua, aku sudah datang"))
# print(today)

email = "capung23@gmail.com"

if validate_email(email):
    print("Email valid gan!")
else:
    print("Email rusak gan!")