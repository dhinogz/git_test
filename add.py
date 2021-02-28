def add(num1, num2):
    return num1 + num2

def printAdd(num1, num2):
    print(str(num1) + " + " + str(num2) + " = " + str(add(num1, num2)))

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

printAdd(num1, num2)