#program created using if, else, elif and string operations which checks the password strength entered by the user.

key=input("Enter Password: ")                                           #takes password input in both numbers and letters
if len(key)<6:                                                          #checks the length of password
    print("Weak Password")
elif key.isdigit():                                                     #checks if password contains only digits

    print("Password should contain numbers and as well as letters")
else:                                                                   #if password length is greater than 6 and contains both digits and letters  
    print("Strong Password")