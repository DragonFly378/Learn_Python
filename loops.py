
# ==> for loops

peoples = ['hafiz', 'ambon', 'kiki', 'ardi']

## Simple for loops
# for person in peoples:
#     print(f"Orang sekarang adalah {person}")

## With Index
# for idx, person in enumerate(peoples):
#     print(f"Orang ke : {idx} adalah {person}")

## Break
# for person in peoples:
#     if person == 'kiki':
#         break
#     print(f"Orang sekarang adalah {person}")

## Continue
# for person in peoples:
    # if person == 'ambon':
    #     continue
    # print(f"Orang sekarang adalah {person}")

## Range
# for i in range(len(peoples)):  
#     print(f"Orang ke-{i} adalah: {peoples[i]}")

# for i in range(0, 12):  
#     print(f"Orang ke-{i}")


# ==> While condition
count = 0 

while count < 10:
    print(f'Count: {count}')
    count += 1