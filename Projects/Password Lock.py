password = input("Please set your password:  ")
print(" \n \n \n \n \n \n \n ")

attempt01 = input("Enter your password please: ")

if attempt01 == password:
    print("Access Granted")
else:
    print("Access Denied\n2/3 attempts remaining\n")
    
    attempt02 = input("Enter your password please: ")
    
    if attempt02 == password:
        print("Access Granted")
    else:
        print("Access Denied\n1/3 attempts remaining\n")
        
        attempt03 = input("Enter your password please: ")
        
        if attempt03 == password:
            print("Access Granted")
        else:
            print("Access Denied\nNo attempts remaining")
            print("Commencing death sequence")



input(" ")
