# If / Else

x = 1
y = 17


# ==> Comparison Operators ( ==, !=, >, <, >=, <=)

## Simple if
# if x < y :
#     print(f"{x} smaller than {y}")

## if / else
# if x < y :
#     print(f"{x} smaller than {y}")
# else: 
#     print(f"{x} greater than {y}")

## elif
# if x < y :
#     print(f"{x} smaller than {y}")
# elif x == y:
#     print(f"{x} equal to {y}")
# else: 
#     print(f"{x} greater than {y}")

## Nested if
# if x > 2:
#     if x <= 10:
#         print(f"{x} greater than 2 and less than or equal to 10")
#     else:
#         print(f"{x} greater than 10")
# else:
#     print(f"{x} less than 2")


# ==> Logical Operators (and, or, not)

## and
# if x > 2 and x <= 10:
#     print(f"{x} greater than 2 and less than or equal to 10")

## or
# if x > 2 or x <= 10:
#     print(f"{x} greater than 2 or less than or equal to 10")

# not
# if not(x == y):
#     print(f"{x} is not equal to {y}")


# ==> Membership operators (in, not in)
# num = 12
# numbers = [2, 5, 7, 12, 20]

## in
# if num in numbers:
#     print(f"{num} is in numbers")
# else:
#     print(f"{num} is not in numbers")

## not in 
# if num not in numbers:
#     print(f"{num} is not member of numbers")
# else:
#     print(f"{num} is in numbers")


# ==> Identity Operators (is, is not)
num = 28
num2 = 20

## is
if num is num2:
    print(f"both is same")
else:
    print(f"both is not same")

## is not
if num is not num2:
    print(f"both is not same")
else:
    print(f"both is same")