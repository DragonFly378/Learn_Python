# Dictionary adalah koleksi yang tidak berurutan, bisa diganti dan memiliki indeks, namun tidak dapat menduplikasi isinya

## Create Dict
person = {
    "first_name" : "Hafiz",
    "last_name" : "Hisbullah",
    "age" :26,
}

print(person)

## User Constructor
# person2 = dict(first_name = "Zaki", last_name = "Nasihuddin", age = 23)
# print(person2)


## Get Value
print(person.get('last_name'))
print(person['last_name'])

## Add key/value
person['phone'] = '0896-1122-3238'
print(person)

## Get dict keys
print(person.keys())

## Get dict items
print(person.items())

## Copy dict
person2 = person.copy()
person2['city'] = "Jakarta"
print(person2)

## Remove item
del(person['age'])
person.pop('phone')
print(person)

## Clear 
person.clear()

## Get Length
print(len(person2))

print(person)

# List of dict
students = [
    {
        'name': "Rizki",
        'age': 21
    },
    {
        'name': "Sifa",
        'age': 25
    }
]

print(students[0]['name'])