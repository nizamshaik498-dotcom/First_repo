#Program made using if, elif, else conditions and using comparision operators in it

User="Jeff bezos"
password=100150

user_name=(input("Enter user name: "))
user_password=int(input("Enter password: "))
if user_name==User and user_password==password:
    print("Login Successfull")
elif user_name==User and user_password!=password:
    print("Wrong password")
else:
    print("User not found")
