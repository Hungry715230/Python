import math

def Help():
    print("Spelling:")
    print("    Circumference, circumference, circ, Circ")
    print("    Pythagorean Theorem, py, Py")
    print("    CircArea, circarea")
def PythagoreanTheorem():
    mode = input("Choose Find Mode: Leg or Hypotenuse")
    if mode == "Hypotenuse" or mode == "hypotenuse":
        leg01 = input("Input leg one:")
        print(" ")
        leg02 = input("Input leg two:")
        print(" ")
        leg01 = int(leg01) ** (2)
        leg02 = int(leg02) ** (2)
        sumleg = leg01 + leg02
        sumleg = math.sqrt(sumleg)
        print(sumleg)
    if mode == "leg" or mode == "Leg":
        leg = input("Input leg:")
        print(" ")
        hypotenuse = input("Input hypotenuse:")
        print(" ")
        leg = int(leg) ** (2)
        hypotenuse = int(hypotenuse) ** (2)
        sumhypotenuse = hypotenuse - leg
        sumhypotenuse = math.sqrt(sumhypotenuse)
        print(sumhypotenuse)
def Circumference():
    pi = math.radians(180)
    r = input("Radius:")
    pi = float(pi)
    r = float(r)
    circ = 2 * pi * r
    print(f"Circumference is {circ}")
def CircleArea():
    pi = math.radians(180)
    r = input("Enter radius:")
    r = float(r)
    pi = float(pi)
    A = pi * r**(2)
    print(f"Area of the circle is {A}")
    

while True:
    action = input("What formula would you like?\nType 'help' for help.")
    if action == "help" or action == "Help":
        Help()
    if action == "Circumference" or action == "circumference" or action == "circ" or action == "Circ":
        Circumference()
    if action == "Pythagorean Theorem" or action == "Py" or action == "py":
        PythagoreanTheorem
    if action == "CircArea" or action == "circarea":
        CircleArea()
