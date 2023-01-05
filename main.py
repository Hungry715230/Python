import random

def encounter_rabbid_dog():
    print("You encounter a rabbid dog! \nWhat do you do?")
def encounter_rat():
    print("You encounter a rat! \nWhat do you do?")
def encounter_infected_rat():
    print("You encounter a infected rat! \nWhat do you do?")

event = random.randint(0, 2)

def encounter_loop():
    if event == 0:
        encounter_infected_rat()
    if event == 1:
        encounter_rat()
    if event == 2:
        encounter_rabbid_dog()