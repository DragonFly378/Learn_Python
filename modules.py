# modules can install using pip package manager

# import datetime
from datetime import date

# pip modules
from camelcase import CamelCase

# today = datetime.date.today()
today = date.today()

# inisiasi p menjadi objek
p = CamelCase()

print(p.hump("halo semua, aku sudah datang"))

print(today)