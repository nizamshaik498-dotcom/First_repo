#program to check while the given input is divisible by 3 and 5 and prints the output
def check_num(num):
    if num %3==0 and num %5==0:
        print(num,"fizz buzz")
    elif num%3==0:
        print(num,"fizz")
    elif num%5==0:
        print(num,"buzz")
    else:
        print("Not divisable by both")
n=int(input("Enter any num:"))
check_num(n)
