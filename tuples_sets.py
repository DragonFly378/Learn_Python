# Tuple adalah koleksi yang berurutan dan tidak dapat diubah, tuple dapat menduplikasi isinya

## Create tuple
numbers = (7, 2, 63, 21, 35, 90)
buah = tuple(('mangga', 'apel', 'anggur', 'pisang'))

## Single value needs trailing comma
buah2 = ('mangga',)


## Can't change value
# buah[0] = "sirsak"
# print(buah)

## Delete tuple
# del buah
# print(buah)

## Get Length
print(len(buah))


# Set adalah koleksi yang tidak berurutan dan tidak berindeks, serta tidak dapat menduplikasi isinya

## Create Set
buah_set = {'mangga', 'apel', 'anggur', 'pisang'}
print(buah_set)

## Add to set
buah_set.add("durian")
print(buah_set)

## Remove from set
buah_set.remove("apel")
print(buah_set)

## Clear ser
buah_set.clear()
print(buah_set)

## Delete 
del buah_set
print(buah_set)