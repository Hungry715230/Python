import math
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
