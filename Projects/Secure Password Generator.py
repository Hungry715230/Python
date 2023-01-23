import string
import random
uppercase = input("Would you like uppercase letters?")
lowercase = input("Would you like lowercase letters?")
special = input("Would you like special characters?")
numbers = input("Would you like numbers?")
a = input("How many characters would you like?")
a = int(a)
if uppercase.lower() == "yes":
    uppercase = True
else:
    uppercase = False
if lowercase.lower() == "yes":
    lowercase = True
else:
    lowercase = False
if special.lower() == "yes":
    special = True
else:
    special = False
if numbers.lower() == "yes":
    numbers = True
else:
    numbers = False
if uppercase and lowercase and special and numbers:
    print("".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range (a)))
if uppercase and lowercase and special and not numbers:
    print("".join(random.choice(string.ascii_letters + string.punctuation) for n in range (a)))
if uppercase and lowercase and numbers and not special:
    print("".join(random.choice(string.ascii_letters + string.digits) for n in range (a)))
if uppercase and numbers and not lowercase and not special:
    print("".join(random.choice(string.ascii_uppercase + string.digits) for n in range (a)))
if uppercase and special and not lowercase and not numbers:
    print("".join(random.choice(string.ascii_uppercase + string.punctuation) for n in range (a)))
if lowercase and numbers and not uppercase and not special:
    print("".join(random.choice(string.ascii_lowercase + string.digits) for n in range (a)))
if lowercase and special and not uppercase and not numbers:
    print("".join(random.choice(string.ascii_lowercase + string.punctuation) for n in range (a)))
if uppercase and lowercase and not numbers and not special:
    print("".join(random.choice(string.ascii_letters) for n in range (a)))
if uppercase and not lowercase and not special and not numbers:
    print("".join(random.choice(string.ascii_uppercase)))
if lowercase and not special and not uppercase and not numbers:
    print("".join(random.choice(string.ascii_lowercase)))
if special and not numbers and not lowercase and not uppercase:
    print("".join(random.choice(string.punctuation)))
if numbers and not special and not lowercase and not uppercase:
    print("".join(random.choice(string.digits)))
