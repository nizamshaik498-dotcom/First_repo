#program created using if, else, while loop (user need to find the special number and if its found he wins or he losses).

num=7
attempts=3
while attempts>0:                                                       #used while loop for multiple attempts
    value=int(input("Enter the special number: "))
    if value==7:
        print("You found the special number🥳")
        break                                                           #used break statement to exit the loop if user finds the special number
    else:
        attempts=attempts-1                                             #decrementing attempts if user fails to find the special number
        print("Ahh its not special🥺")
        print("Attempts Left: ",attempts)                               #printing remaining attempts
        if attempts==0:                                              #checking if attempts are over                                 
            print("Game Over❌❌")



