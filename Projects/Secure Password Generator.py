import random
import string
action = input("Do you want a secure password? (y / n)")
if action.lower() == "y":
    print("Okay\n")
    randomString = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(20)])
    print(randomString)
else:
    print("\nI is sad")
