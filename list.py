#program using list and asking user to input values in the empty list and using loop 

Numbers=[]
n=int(input("Enter the number of elements you want to add to the list: "))
for i in range(n):
    element=int(input("Enter element {}: ".format(i+1)))
    Numbers.append(element)
print("The complete list is:", Numbers)                         #displaying the list
print("The length of the list is:", len(Numbers))               #displaying the length of the list
print("The sum of the list elements is:", sum(Numbers))         #displaying the sum of the list elements

