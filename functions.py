# Create Function
def sayHello(name):
    print(f'Hello {name}')

sayHello("Putri")

def getSum(num1, num2, num3):
    nums = [num1, num2, num3]
    total = num1 + num2 + num3
    return total

num = getSum(2, 5, 4)
print(num)


# Lambda function is a small anonymous function.
# Lambda function can take any number of arguments, but can only have one espression

getDiff = lambda num1, num2: num1 - num2

res = getDiff(6,2)
print(res)