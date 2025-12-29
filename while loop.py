#program to print numbers from 1 to 20using a while loop and skiping numbers divisible by 3
num = 1
while num <= 20:
    if num % 3 != 0:
        print(num)
    num += 1
    