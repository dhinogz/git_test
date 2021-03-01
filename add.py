def add(num1, num2):
    return num1 + num2

def dispAdd():
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")

dispAdd()