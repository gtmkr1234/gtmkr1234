NamesOFClients = ['Arshika Gupta', 'Hitansh Goswami', 'Himanshi', 'Harshita', 'Hitakshi', 'Tanya', 'Alisha']
ClientPins = ['0001', '0002', '0003', '0004', '0005', '0006', '0007']
ClientBalances = [10000, 20000, 30000, 40000, 50000, 60000, 70000]
ClientDeposition = 0
ClientWithdrawal = 0
ClientBalance = 0
disk1 = 1
disk2 = 7
u = 0
while True:
# os.system("cls")
print("********************")
print("========== WELCOME TO BANKING SYSTEM ==========")
print("********************")
print("========== (a). Open New Client Account ============")
print("========== (b). The Client Withdraw a Money ============")
print("========== (c). The Client Deposit a Money ============")
print("========== (d). Check Clients &amp; Balance ============")
print("========== (e). For Loan in our Bank ==========")
print("========== (f). For Policy in our Bank ==========")
print("========== (g). For Modify the Account Details ============")
print("========== (h). For Deleting a Account ============")
print("========== (i). For Face Detection ============")
print("========== (j). Call center (for Contacting) ============")
print("========== (k). FAQs (Frequent Asked Question) ============")
print("========== (l). FeedBack Form ============")
print("========== (m). Quit ============")
print("********************")

EnterLetter = input("Select a Letter from the Above Box menu : ")
if EnterLetter =="a" :
print(" Letter a is Selected by the Client")
NumberOfClient = eval(input("Number of Clients : "))
u = u + NumberOfClient

if u > 7:
print("\n")
print("Client registration exceed reached or Client registration too low")
u = u - NumberOfClient
else:
while disk1 <= u:
name = input("Write Your Fullname : ")
NamesOFClients.append(name)
pin = str(input("Please Write a Pin to Secure your Account : "))
ClientPins.append(pin)
ClientBalance = 0
ClientDeposition = eval(input("Please Insert a Money to Deposit to Start an Account : "))
ClientBalance = ClientBalance + ClientDeposition
ClientBalances.append(ClientBalance)
print("\nName=", end=" ")
print(NamesOFClients[disk2])
print("Pin=", end=" ")
print(ClientPins[disk2])
print("Balance=", "P", end=" ")
print(ClientBalances[disk2], end=" ")
disk1 = disk1 + 1
disk2 = disk2 + 1
print("\nYour name is added to Client Table")
print("Your pin is added to Client Table")
print("Your balance is added to Client Table")
print("----New Client account created successfully !----")
print("\n")
print("Your Name is Available on the Client list now : ")
print(NamesOFClients)
print("\n")
print("Note! Please remember the Name and Pin")
print("========================================")

mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "b":
v = 0
print(" letter b is Selected by the Client")
while v < 1:
w = -1
name = input("Please Insert a name : ")
pin = input("Please Insert a pin : ")
while w < len(NamesOFClients) - 1:
w = w + 1
if name == NamesOFClients[w]:
if pin == ClientPins[w]:
v = v + 1
print("Your Current Balance:", "P", end=" ")
print(ClientBalances[w], end=" ")
print("\n")
ClientBalance = (ClientBalances[w])
ClientWithdrawal = eval(input("Insert value to Withdraw : "))
if ClientWithdrawal > ClientBalance:
deposition = eval(input(
"Please Deposit a higher Value because your Balance mentioned above is not enough : "))
ClientBalance = ClientBalance + deposition
print("Your Current Balance:", "P", end=" ")
print(ClientBalance, end=" ")
ClientBalance = ClientBalance - ClientWithdrawal
print("-\n")
print("----Withdraw Successfully!----")
ClientBalances[w] = ClientBalance
print("Your New Balance: ", "P", ClientBalance, end=" ")
print("\n\n")
else:
ClientBalance = ClientBalance - ClientWithdrawal
print("\n")
print("----Withdraw Successfully!----")
ClientBalances[w] = ClientBalance
print("Your New Balance: ", "P", ClientBalance, end=" ")
print("\n")
if v < 1:
print("Your name and pin does not match!\n")
break

mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "c":
print("Letter c is selected by the Client")
x = 0
while x < 1:
w = -1
name = input("Please Insert a name : ")
pin = input("Please Insert a pin : ")
while w < len(NamesOFClients) - 1:
w = w + 1
if name == NamesOFClients[w]:
if pin == ClientPins[w]:
x = x + 1
print("Your Current Balance: ", "P", end=" ")
print(ClientBalances[w], end=" ")
ClientBalance = (ClientBalances[w])
print("\n")
ClientDeposition = eval(input("Enter the value you want to deposit : "))
ClientBalance = ClientBalance + ClientDeposition
ClientBalances[w] = ClientBalance
print("\n")
print("----Deposition successful!----")
print("Your New Balance: ", "P", ClientBalance, end=" ")
print("\n")
if x < 1:
print("Your name and pin does not match!\n")
break

mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "d":
print("Letter d is selected by the Client")
w = 0
print("Client name list and balances mentioned below : ")
print("\n")
while w <= len(NamesOFClients) - 1:
print("->;.Customer =", NamesOFClients[w])
print("->;.Balance =", "P", ClientBalances[w], end=" ")

print("\n")
w = w + 1

mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "e":
print("letter e is selected by the client")
print(" 1) types of loan (for better understanding)")
print(" 2) directly apply for loan")
choice = input("enter your choice from above -")
if choice == "1":
print("Bank of Baroda offers a wide range of loans to meet your diverse needs. ")
print("Whether the need is for a house, child's education, our unique and need specific loans will enable you to convert your dreams to realities.")
print("=====There are basically six types of loans depending on your needs.====")
print("Name of the loans are:")
print("1. VEHICLE LOAN - ")
print(" Plan for a smooth and easy journey without any speedbumps. ")
print(" Apply for Vehicle Loan and get quick approvals at our Bank. ")
print(" In this you have to pay 2% of interest per month. ")
print("2. GOLD LOAN - ")
print(" Urgent need of cash?")
print(" Gold Loans from Bank of Baroda is your definitive solution to meet your financial needs.")
print(" Apply for Gold Loan and get quick approvals at our Bank.")
print(" In this you have to pay 3% of interest per month.")
print("3. HOME LOAN - ")
print(" Are you are dreaming of buying your own residence?")
print(" Opt for BSA Bank Home Loan.")
print(" Our bob home loan is packed with several exclusive features and benefits for aspiring homeowners.")
print(" Our housing loan can be used for a variety of purposes.")
print(" For instance, you can buy a plot, purchase a flat, build your own home and even extend your existing residence with a home loan.")
print(" Use the bank home loan calculator to find out BSA Bank home loan interest rate & more! ")
print(" In this you have to pay 2.5% of interest per month")
print("4. PERSONAL LOAN -")
print(" Personal loans from Bank offer quick and easy solution to all your urgent financial needs.")
print(" Whether you need funds for a medical emergency in your family, your sibling’s wedding, or to renovate your home, a personal loan can finance all your requirements.")
print(" Personal loans have many advantages over other forms of credit, such as untrustworthy financiers. ")
print(" Most salaried persons, self-employed and professionals can apply for personal loans.")
print(" With attractive interest rates, speedy processing, Bank offers among best personal loans today.")
print(" In this you have to pay 1.5% of interest per month ")
print(" 5. EDUCATION LOAN - ")
print(" Why should finance come in the way of future?")
print(" Getting an education loan is an easy way to finance your dreams.")
print(" A student loan can help you get into the university of your choice.")
print(" Bank of Baroda is here to finance your dreams, education & career goals.")
print(" In this you have to pay 1% of interest per month ")
print("6. FINTECH - ")
print(" A credit that encompasses all credit activity facilitated by electronic platforms.")
print(" At Bank of Baroda borrowers are matched directly with lenders.")
print(" Receive benefits such as loan-based or marketplace lending through Fintech Loans from Bank.")
print(" In this you have to pay 4% of interest per month ")
print("Thanks for visting this page. Hope this will help you")
print("For more details contact to us through website or call")
elif choice == "2":
print("i) VEHICLE loan \nii)GOLD loan \niii) HOME loan \niv) PERSONAL loan \nv) EDUCATION loan \nvi) FINTECH")
typeofloan = input("enter the type of loan you want => ")
name = input("enter your name => ")
if typeofloan == "i":
print("Thanks for choosing vehicle loan.")
amount = input("How much amount of loan you want =")
percent = 0.02
print("The interest on this loan is 2%.")
interest = float(amount) * float(percent)
amount_to_submit = float(amount) + float(interest)
print(f"The amount you have to pay - {amount_to_submit}")
elif typeofloan == "ii":
print("Thanks for choosing gold loan.")
amount = input("How much amount of loan you want =")
percent = 0.03
print("The interest on this loan is 3%.")
interest = float(amount) * float(percent)
amount_to_submit = float(amount) + float(interest)
print(f"The amount you have to pay - {amount_to_submit}")
elif typeofloan == "iii":
print("Thanks for choosing home loan.")
amount = input("How much amount of loan you want =")
percent = 0.025
print("The interest on this loan is 2.5%.")
interest = float(amount) * float(percent)
amount_to_submit = float(amount) + float(interest)
print(f"The amount you have to pay - {amount_to_submit}")
elif typeofloan == "iv":
print("Thanks for choosing personal loan.")
amount = input("How much amount of loan you want =")
percent = 0.015
print("The interest on this loan is 1.5%.")
interest = float(amount) * float(percent)
amount_to_submit = float(amount) + float(interest)
print(f"The amount you have to pay - {amount_to_submit}")
elif typeofloan == "v":
print("Thanks for choosing education loan.")
amount = input("How much amount of loan you want =")
percent = 0.01
print("The interest on this loan is 1%.")
interest = float(amount) * float(percent)
amount_to_submit = float(amount) + float(interest)
print(f"The amount you have to pay - {amount_to_submit}")
elif typeofloan == "vi":
print("Thanks for choosing fintech.")
amount = input("How much amount of loan you want =")
percent = 0.04
print("The interest on this loan is 4%.")
interest = float(amount) * float(percent)
amount_to_submit = float(amount) + float(interest)
print(f"The amount you have to pay - {amount_to_submit}")

mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")

elif EnterLetter == "f":
print("letter f is selected by the client")

mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "g":
print("letter g is selected by the client")
print("The details you can change are as follows:-")
print("1 for Name")
print("2 For Contact No.")
print("3 For Address")
print("4 For Nominee")
change = int(input("Enter your choice that you want to change-"))
if change == 1:
Old_name = input("Enter your old Name- ")
New_name = input("Enter your new Name- ")
print("Thank you! Your Name has changed. ")

elif change == 2:
Old_Contact_No = input("Enter your old Contact No.- ")
New_Contact_No = input("Enter your new Contact No.- ")
print("Thank you! Your Contact No. has changed. ")

elif change == 3:
Old_Address = input("Enter your old Address- ")
New_Address = input("Enter your new Address- ")
print("Thank you! Your Address has changed. ")

elif change == 4:
Old_Nominee = input("Enter your old Nominee- ")
New_Nominee = input("Enter your new Nominee- ")
print("Thank you! Your Nominee has changed. ")

else:
print("Invalid choice!")

mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "h":
print("letter h is selected by the client")
Name = input("Enter the name whose account you want to delete")
Pin = input("please insert the pin also")
Number = input("enter your contact no. also")
print("your account has been deleted.")

mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "i":
print("letter i is selected by the client")
##import numpy as np
import cv2

detector = cv2.CascadeClassifier('faceial.xml')

cap = cv2.VideoCapture(0)

while (True):
ret, img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = detector.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 4)

cv2.imshow('frame', img)
if cv2.waitKey(1) == ord('q'):
break

cap.release()
cv2.destroyAllWindows()

mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "j":
print("letter j is selected by the client")
print("We provide two policies to our costumers.")
print("")


def callcentre():
print("please select one of the following :")
print("Press 1 to register your complain")
print("Press 2 for Details of various offers on loans")
print("Press 3 for our exchange policy")
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
while (line1 != ""):
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

mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "k":
print("letter k is selected by the client")
print("Here are some most frequently asked questions")
print("1.Can I change the details of my bank account?")
print("2.Why should I give my bank account details at the time of account opening?")
print("3.What is the procedure to claim the amount?")
print("4.What is the age criteria for availing loans ?")
print("5.Can the nominee be changed?")
print("6.Who can apply for the loan?")
print("7.What is the mode of repayment?")
print("8.Do you offer any concessions?")
print("9.What actions are taken for the security of my account, if my card is lost?")
print("10.What is smart card?")
question = int(input("Enter the number from above whose ans you want to know-"))
if question == 1:
print("Yes. Since in the depository system monetary benefits on your security balances are paid as per the bank account details provided by you at the time of account opening, you must ensure that any subsequent change in bank account details is informed to your depository participant.")
elif question == 2:
print("It is for the protection of your interest. Your bank account number will be mentioned on the interest or dividend warrant you are entitled to so that such warrant cannot be encashed by anyone else. Further, a DP cannot open the account if the bank account number is not given.")
elif question == 3:
print("Visit the branch with KYC documents and fill the required form.")
elif question == 4:
print("Minimum age criteria for availing Agri Loans is 18 years and maximum up to 70 years as on the date of availing facility. If the age of land holder exceeds 70 years, in such case the legal heirs to be made co borrowers")
elif question == 5:
print("Yes, the nomination can be changed anytime by the account holder/s by simply filling up the nomination form once again and submitting it to the branch DP.")
elif question == 6:
print("Any Indian National fulfilling the criteria stated above is eligible for education loan")
elif question == 7:
print("The accrued interest during the repayment holiday period to be added to the principal and repayment in Equated Monthly Instalment (EMI) is fixed.")
elif question == 8:
print("Yes, we do offer 1% interest concession to student loanee, if the interest is serviced during the study period when the repayment holiday is specified for interest/repayment under the scheme. Additionally, 1% interest concession is provided to girl students")
elif question == 9:
print("If the card is lost you should report to the base branch/control centre immediately. Base branch will intimate the message to Baroda Omni control centre and your card will be hotlisted. Once a card is hotlisted that card cannot be used anywhere else")
elif question == 10:
print("Other than the cardholder, nobody else can use the smart card. Smart card identifies the customer in four different ways photograph, signature, personal identification number i.e. his secret PIN and online verification of his account. PINs are to be kept secret.")
else :
print("Please write your question. You will get your ans as soon as possible on your e-mail id.")
Your_ques = input ("Write your question here-")
Your_email_id = input ("Enter your mail id-")
print ("You will get your ans definetly.\n Thank you for your patience ")

mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "l":
print("letter l is selected by the client")
print("Please rate to our banking management system")
Rating = int(input("How much rating you will give to BSA Bank"))
Suggestions = input("How can we improve this?")
print("Your reply has been submitted")

mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")

elif EnterLetter == "m":
print("letter m is selected by the client")
print("Thank you for using our banking system!")
print("\n")
print("Thank You and Come again")
print("God Bless")
break
else:
print("Invalid option selected by the Client")
print("Please Try again!")

mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")