import time
def greet():
    print("---  Welcome to Livewire Portal  ---")
    
def menu():
    menu = {1:"Registration",2:"Fees Payment",
            3:"Certificate Generate",4:"Upcoming Placement",
            5:"Add On Session Availability",6:"Exit"}
    print("\n       How Can I Help You??\n")
    print("--------------------------------------")
    for i in menu:
        
        print(i,".",menu[i])
        time.sleep(0.5)
    print("--------------------------------------")
    choice(menu)
def choice(menu):
    ch = int(input("Enter The Choice (1/2/3/4/5/6) : "))
    if ch==1:
        registration()
    elif ch==2:
        feesPayment()
    elif ch==3:
        certificate()
    elif ch==4:
        placement()
    elif ch==5:
        session()
    elif ch==6:
        print("Thank You For Visiting Our Site !!")
        import sys
        sys.exit(0)
    else:
        print("Invalid Option . Please Re-Enter The Choice !! \n")
        menu()
def registration():
    print("---  REGISTRATION PANEL  ---")
    import registration as r
    r.details()
    menu()
def feesPayment():
    print("---  FEES PAYMENT PANEL  ---")
    menu()
def certificate():
    print("---  CERTIFICATE PANEL  ---")
    menu()
def placement():
    print("---  PLACEMENT PANEL  ---")
    menu()
def session():
    print("---  ADD-ON SESSION PANEL  ---")
    menu()

greet()
menu()




def details():
    name = input("Enter Your Name : ")
    for i in name:
        if not((i>='a' and i<='z') or (i>='A' and i<='Z') or (i==' ')):
            print("Your Name Containing Symbols / Number \nPlease Re-Enter The Name")
            name = input("Enter Your Name : ")
            break
    phoneNumber = int(input("Enter Your Phone Number : "))
    if not(phoneNumber>=6000000000 and phoneNumber<=9999999999):
        print("Your Mobile Number is less / more than 10 digits \nPlease Re-Enter The Mobile Number")
        phoneNumber = int(input("Enter Your Phone Number : "))
    mailid = input("Enter Your Mail Id : ")
    if not(mailid.endswith("@gmail.com") and mailid.islower()):
        print("Your Mail Id Is Invalid \nPlease Re-Enter The Mail Id")
        mailid = input("Enter Your Mail Id : ")
    courseList = {
        1:{"courseName":"Master In AI Developer Certification","courseFee":45000,"onlineFee":25000,"cashFee":20000},
        2:{"courseName":"Master In Python Developer Certification","courseFee":16000,"onlineFee":10000,"cashFee":6000},
        3:{"courseName":"Master In Full Stack Developer Certification","courseFee":37000,"onlineFee":25000,"cashFee":12000},
        4:{"courseName":"Master In Cyber Security Analyst Certification","courseFee":42000,"onlineFee":25000,"cashFee":17000}}
    for i in courseList:
        print(i,"Course Name : ",courseList[i]["courseName"])
        print("Course Total Payment : ",courseList[i]["courseFee"])
        print("Course Total Payment : ",courseList[i]["onlineFee"])
        print("Course Total Payment : ",courseList[i]["cashFee"])
    course = input("Enter The Course Name (1/2/3/4): ")
    confirm = input("Please Confirm The Registration By Entering ('Yes') : ")
    if confirm.lower() == 'yes':
        print("Thank You For Choosing This Course!!")
    else:
        print("Thank You Visiting !! Come Again")
    
    

