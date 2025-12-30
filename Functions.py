#program to check while the given input is divisible by 3 and 5 and prints the output

check_num=int(input("Enter any num:"))
if check_num %3==0 and check_num %5==0:
    print(check_num,"fizzbuzz")
elif check_num %3==0:
    print(check_num,"fizz")
elif check_num %5==0:
    print(check_num,"buzz")
else:
    print("Not divisable by both")