def callcentre():
    print("please select one of the following :")
    print("Press 1 to register your complain")
    print("Press 2 for Details of various offers on branded products")
    print("Press 3 for our exchange scheme")
    a = int(input())
    if a == 1:
        comp()
        print("Your complain has been registered successfully")
        b = int(input("press 1 for main menu :"))
        if b == 1:
            callcentre()

    elif a == 2:
        prod()
        b = int(input("press 1 for main menu :"))
        if b == 1:
            callcentre()

    elif a == 3:
        exch()
        print("Your request has been saved we will revert you soon")
        b = int(input("press 1 for main menu :"))
        if b == 1:
            callcentre()

    else:
        print("Invalid Entry")
        first()


def comp():
    nam = input("Enter your complain :")
    f = open('a.txt', 'a')
    f.write(nam)
    f.close()


def prod():
    f = open('offer.txt', 'r')
    line = f.readline()
    while line != "":
        print(line)
        line = f.readline()
    f.close()


def exch():
    nam = str(input("Please enter the details of your products which you want exchange"))
    f = open('exch.txt', 'a')
    f.write(nam)
    f.close()


def first():
    print("welcome to All india Customer service")
    print("please confirm your id")
    print("1.Administrator")
    print("2.Customer")

    a = int(input("Please enter your input: "))
    if a == 1:
        b = int(input("To view the complains press 1 : "))
        if b == 1:
            file = open("a.txt", 'r')
            line1 = file.readline()
            while(line1!=""):
                print(line1)
                line1 = file.readline()
            file.close()
            print(" ")
            first()
        else:
            first()

    if a == 2:
        callcentre()

    else:
        print("Invalid Entry")
        first()


first()
