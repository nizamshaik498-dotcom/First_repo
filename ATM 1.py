#program created using if, else, elif conditions (ATM system) with getting 3 attempts for user

username="admin"
password=1234
attempts=3

while attempts>0:
    name=input("Enter Username: ")
    pin=int(input("Enter Password: "))
    if name==username and pin==password:
        print("Login Successfull")
        break
    else:
        attempts=attempts-1
        print("Wrong Credentials")
        print("Attempts Remaining: ",attempts)
    if attempts==0:
        print("Account Locked")

