#progam using for loop and else condition

numbers=[10,20,30,40,50]                    #list of numbers
find=int(input("Enter any value: "))
for n in numbers:                           #used for loop 
    if n==find:
        print("Number found")
        break                               #used break statement
    else:                                   #used else condition with for loop
        print("Number not found")
        break