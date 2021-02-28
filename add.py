def add(num1, num2):
    return num1 + num2

def dispAdd():
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print(str(num1) + " + " + str(num2) + " = " + str(add(num1, num2)))



dispAdd()