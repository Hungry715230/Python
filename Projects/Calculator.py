print("I is a calculator with only add, subtract, divide and multiply functions, all functions are spelling-sensitive.")

def Add():
    add01 = input("Number one you want to add:")
    add02 = input("Number two you want to add:")
    print(" ")
    AddResult = int(add02) + int(add01)
    print(f"{add01} + {add02} = {AddResult}")
    print(" ")
def Subtract():
    subtract01 = input("Number one you want to subtract:")
    subtract02 = input("Number two you want to subtract:")
    print(" ")
    SubtractResult = int(subtract01) - int(subtract02)
    print(f"{subtract01} - {subtract02} = {SubtractResult}")
    print(" ")
def Multiply():
    multiply01 = input("Number one you want to multiply:")
    multiply02 = input("Number two you want to multiply:")
    print(" ")
    MultiplyResult = int(multiply01) * int(multiply02)
    print(f"{multiply01} * {multiply02} = {MultiplyResult}")
    print(" ")
def Divide():
    divide01 = input("Number one you want to divide:")
    divide02 = input("Number two you want to divide:")
    print(" ")
    DivideResult = int(divide01) / int(divide02)
    print(f"{divide01} / {divide02} = {DivideResult}")
    print(" ")

while True:
    desicion = input("What action would you like to take?")
    if desicion == "add" or desicion == "Add":
        Add()
    if desicion == "subtract" or desicion == "Subtract":
        Subtract()
    if desicion == "multiply" or desicion == "Multiply":
        Multiply()
    if desicion == "divide" or desicion == "Divide":
        Divide()
