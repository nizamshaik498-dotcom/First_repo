#progam using for loop and else condition

numbers=[10,20,30,40,50]
find=int(input("Enter any value: "))
for n in numbers:
    if n==find:
        print("Number found")
        break
    else:
        print("Number not found")
        break