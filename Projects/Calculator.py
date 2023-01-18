import math

print("I is a calculator with add, subtract, divide, multiply, square root and power functions, all functions are spelling-sensitive. Type 'help' for help")

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
def Power():
    power01 = input("Base number: ")
    power02 = input(f"{power01} to the power of: ")
    print(" ")
    PowerResult = int(power01) ** int(power02)
    print(f"{power01} to the power of {power02} is {PowerResult}")
    print(" ")
def Sqrt():
    number01 = input("What would you like the square root of: ")
    print(" ")
    SqrtResult = math.sqrt(int(number01))
    print(f"The square root of {number01} is {SqrtResult}")
    

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
    if desicion == "pow" or desicion == "power" or desicion == "Power" or desicion == "Pow":
        Power()
    if desicion == "sqrt" or desicion == "Square root" or desicion == "square root" or desicion == "Square Root" or desicion == "Sqrt":
        Sqrt()
    if desicion == "help" or desicion == "Help":
        print("Functions:")
        print("    Add, spelling: add, Add, addition, Addition")
        print("    Subtract, spelling: subtract, Subtract, sub, Sub")
        print("    Multiply, spelling: multiply, Multiply, mult, Mult")
        print("    Divide, spelling: divide, Divide, div, Div")
        print("    Power, spelling: power, Power, pow, Pow")
        print("    Square Root, spelling: sqrt, Sqrt, square root, Square root, Square Root")
        print("    Help, spelling: help, Help")
