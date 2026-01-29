#program created using list which stores the values given by user in it and shows largest, smallest and average of the values
num=list(map(int,input("Enter numbers: ").split())) 
largest=max(num)
smallest=min(num)
average=sum(num)/len(num)
print("The largest number is: ",largest)
print("The smallest number is: ",smallest)
print("The average is : ",average)