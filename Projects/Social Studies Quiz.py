import random

global score
score = 0

#Defines Functions
def ask01():
        global score
        answer01 = input("First written plan of government for the US. ")
        if answer01 == "Articles of Confederation":
            print("Correct")
            score = score + 1
        else:
            print("Incorrect")
def ask02():
        global score
        answer02 = input("Governing system of a union of states.  ")
        if answer02 == "Federal Government":
            print("Correct")
            score+=1
        else:
            print("Incorrect")
def ask03():
        global score
        answer03 = input("A series of 85 essays written under the name Publius to promote ratification of the U.S. Constitution.  ")
        if answer03 == "Federalist Papers":
            print("Correct")
            score+=1
        else:
            print("Incorrect")
def ask04():
        global score
        answer04 = input("The house of Congress where representation is equal - 2 senators per state  ")
        if answer04 == "Senate":
            print("Correct")
            score+=1
        else:
            print("Incorrect")
def ask05():
        global score
        answer05 = input("National law-making body  ")
        if answer05 == "Congress":
            print("Correct")
            score+=1
        else:
            print("Incorrect")
def ask06():
        global score
        answer06 = input("The head of a government  ")
        if answer06 == "Chief Executive":
            print("Correct")
            score+=1
        else:
            print("Incorrect")
def ask07():
    global score
    answer07 = input("The group established by the Constitution to elect the president and vice president  ")
    if answer07 == "Electoral College":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask08():
    global score
    answer08 = input("The plan that called for government with 3 branches, but the legislative branch would have one house (part), favored by small states because each state would have equal numbers of representatives  ")
    if answer08 == "New Jersey Plan":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask09():
    global score
    answer09 = input("The agreement that established that slaves would be counted as 3/5ths of a person when determining state representation in the House of Representatives and taxation  ")
    if answer09 == "3/5 Compromise" or answer09 == "3/5ths Compromise":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask10():
    global score
    answer10 = input("The house of Congress where representation is based on state population")
    if answer10 == "House of Representatives  ":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask11():
    global score
    answer11 = input("Region of the United States bounded by the Ohio and Mississippi Rivers and the Great Lakes. The region was given to the U.S. by the Treaty of Paris 1783.  ")
    if answer11 == "Northwest Territory":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask12():
    global score
    answer12 = input("A law passed by Congress in 1787 that specified how western lands would be governed  ")
    if answer12 == "Northwest Ordinance":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask13():
    global score
    answer13 = input("Supreme power or authority  ")
    if answer13 == "Sovereignty":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask14():
    global score
    answer14 = input("A person sent or authorized to represent others  ")
    if answer14 == "Delegate":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask15():
    global score
    answer15 = input("The supreme law of the land, governing document of the USA  ")
    if answer15 == "U.S. Constitution":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask16():
    global score
    answer16 = input("Massachusetts farmers rebelled against taxes in 1786 making Americans believe the nation was falling apart  ")
    if answer16 == "Shays Rebellion":
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")
def ask17():
    global score
    answer17 = input("To settle a conflict by each group giving up something and each group getting something  ")
    if answer17 == "Compromise":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask18():
        global score
        answer18 = input("A country governed by elected officials  ")
        if answer18 == "Republic":
            print("Correct")
            score+=1
        else:
            print("Incorrect")
def ask19():
        global score
        answer19 = input("The name that James Madison, John Jay, and Alexander Hamilton used to write the Federalist Papers  ")
        if answer19 == "Publius":
            print("Correct")
            score+=1
        else:
            print("Incorrect")
def ask20():
        global score
        answer20 = input("An organized group having the authority to make laws  ")
        if answer20 == "Legislature":
            print("Correct")
            score+=1
        else:
            print("Incorrect")
def ask21():
        global score
        answer21 = input("Philadelphia 1787, meeting where delegates wrote the US Constitution  ")
        if answer21 == "Constitutional Convention":
            print("Correct")
            score+=1
        else:
            print("Incorrect")
def ask22():
    global score
    answer22 = input("James Madison’s  plan that called for a strong central government with 3 branches, the legislative branch having two houses (parts) House of Representatives and Senate, favored by large states who would have more representatives  ")
    if answer22 == "Virginia Plan":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask23():
    global score
    answer23 = input("Plan established a two-house congress, the House of Representatives and the Senate. House of Representatives would be based on state population and the Senate would have equal representation per state  ")
    if answer23 == "Great Compromise":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask24():
    global score
    answer24 = input("Supporter of the Constitution  ")
    if answer24 == "Federalist":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask25():
    global score
    answer25 = input("Officially approve  ")
    if answer25 == "Ratify":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask26():
    global score
    answer26 = input("Opponent of the Constitution  ")
    if answer26 == "Anti-Federalist":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask27():
    global score
    answer27 = input("Dealing with or relating to other countries  ")
    if answer27 == "Foreign":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask28():
    global score
    answer28 = input("A person who creates a plan (the people who created the Constitution)  ")
    if answer28 == "Framers":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask29():
    global score
    answer29 = input("A tax to be paid on a particular import or export  ")
    if answer29 == "Tariff":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
def ask30():
    global score
    answer15 = input("A government set up to have limited power of its citizens  ")
    if answer15 == "Limited government":
        print("Correct")
        score+=1
    else:
        print("Incorrect")


print("This is a program to test your vocab, let's get started\nAlso, it is case-senstitive and spelling is crucial. Good Luck!\n")

question = 0
i = 0
while i < 31:
    if question == 1:
        ask01()
    if question == 2:
        ask02()
    if question == 3:
        ask03()
    if question == 4:
        ask04()
    if question == 5:
        ask05()
    if question == 6:
        ask06()
    if question == 7:
        ask07()
    if question == 8:
        ask08()
    if question == 9:
        ask09()
    if question == 10:
        ask10()
    if question == 11:
        ask11()
    if question == 12:
        ask12()
    if question == 13:
        ask13()
    if question == 14:
        ask14()
    if question == 15:
        ask15()
    if question == 16:
        ask16()
    if question == 17:
        ask17()
    if question == 18:
        ask18()
    if question == 19:
        ask19()
    if question == 20:
        ask20()
    if question == 21:
        ask21()
    if question == 22:
        ask22()
    if question == 23:
        ask23()
    if question == 24:
        ask24()
    if question == 25:
        ask25()
    if question == 26:
        ask26()
    if question == 27:
        ask27()
    if question == 28:
        ask28()
    if question == 29:
        ask29()
    if question == 30:
        ask30()
    question = random.randint(0, 30)
    i+=1
    print(" ")

print("You got " + str(score) + "/30 correct")
