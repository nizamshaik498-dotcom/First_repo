#program made using sets and prints the union, intersection and difference of two setss by taking input from the user

num1 = int(input("Enter the number of elements in the first set: "))
set1 = set()
for i in range(num1):
    element = input("Enter element {}: ".format(i + 1))
    set1.add(element)
num2 = int(input("Enter the number of elements in the second set: "))
set2 = set()
for i in range(num2):
    element = input("Enter element {}: ".format(i + 1))
    set2.add(element)
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
print("Union of the two sets: ", union_set)
print("Intersection of the two sets: ", intersection_set)
print("Difference of the two sets (set1 - set2): ", difference_set)
