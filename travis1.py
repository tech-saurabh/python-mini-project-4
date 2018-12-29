known_users=["Saurabh","Saurya","shikha","Sumit","Garima","Mayank","Smith","Emma"]
print(len(known_users))
while True:
    print("Hi! My name is travis ")
    name=input("what is your name : ").strip().capitalize()
    if name in known_users:
        print("Hello {} welcome to the security system".format(name))
        remove=input("Would you want to be removed from the system (y/n)  : ").lower()
        if(remove=="y"):
            known_users.remove(name)
        elif(remove=="n"):
            print("no problem i don't want you to leave")
    else:
        print("hmm! i dont think i have  met you yet {} ".format(name))
        add_me=input("Would you like to be added to be the system (y/n) : ").lower()
        if(add_me=="y"):
            known_users.append(name)
        elif(add_me=="n"):
            print("no worries, see you around! ")
