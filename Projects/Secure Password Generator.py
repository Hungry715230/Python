import random
import string
action=input("Do you want a secure password? (y / n)")
if action.lower()=="y"or action.lower()=="yes":
    print("Okay\n")
    randomString=''.join([random.choice(string.ascii_letters+string.digits+string.punctuation)for n in range(20)])
    print(randomString)
else:
    print("\nHere is your unsecure password:\n\nAB123456789")
