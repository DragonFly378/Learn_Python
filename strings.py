

# String Formatting

name = 'joko'
age = 23

## Concatenate
# print("hello nama saya " + name + "umur saya " + str(age))

## Arguments by positions
# print("hello my name is {nama}, and i am {umur} years old".format(nama=name, umur=age))

## F-Strings (3.6+)
# print(f'hello my name is {name}, and i am {age} years old')

''' <===================>  '''


# String Methods

s = "Perkenalkan kepada Dunia"

## Capitalize string
print(s.capitalize())

## Uppercase all
print(s.upper())

## Make all lower
print(s.lower())

## Swap case
print(s.swapcase())

## length strings
print(len(s))

## Replace 
print(s.replace('Dunia', "Capung"))

## Count
sub = 'a'
print(s.count(sub))

## Starts with
print(s.startswith('hello'))

## Ends with
print(s.endswith('Dunia'))

## Split into List
print(s.split())

## Find position 
print(s.find('a'))

## Is all alphanumeric
print(s.isalnum())

## Is all alphabetic
print(s.isalpha())

## Is all numeric
print(s.isnumeric())