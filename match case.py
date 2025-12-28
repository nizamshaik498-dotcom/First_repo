#program using matchcase by taking input from user and printing week days

user_input=int(input("Enter any number between 1 to 7:"))
match user_input:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

