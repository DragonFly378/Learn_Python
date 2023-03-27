
## Create list
numbers = [7, 2, 63, 21, 35, 90]
buah = ['mangga', 'apel', 'anggur', 'pisang']

## Create with constructor
numbers2 = list((3, 5, 12, 53, 33))
print(buah, numbers2)

## Get a value
print(buah[0])

## Get length
print("length: ", len(buah))

## Append to list
buah.append('sirsak')
print("append: ", buah)

## Remove from list
buah.remove("apel")
print("remove: ", buah)

## Insert into Position
buah.insert(2, 'srikaya')
print("insert: ", buah)

## Change value
buah[0] = "Durian"
print("change value: ", buah)

## Remove with pop
buah.pop(3)
print("pop: ", buah)

## Reverse list
buah.reverse()
print("reverse: ", buah)

## Sort List
numbers2.sort()
print("sort: ", numbers2)

## Reverse sort list
numbers2.sort(reverse=True)
print("sort reverse: ", numbers2)

