class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        print(f'My name is {self.name} and I am {self.age} years old')


    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old'

    def has_birthday(self, num):
        self.age += num


# Extend Class
class Customer (User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old and my balance is {self.balance}'





# Inisiaasi User object
brad = User("Capung Berjaya", "capung23@gmail.com", 21)
# brad.has_birthday(3)

print(brad)

# Inisiasi Customer object
handi = Customer("Handi", "handigunadi@gmail.com", 18)
handi.set_balance(40)
handi.has_birthday(2)

# print(handi.greeting())






