#program created by using f-strings and take input from user and print the output

name=input("Enter your name: ")               #taking name as input from user
age=int(input("Enter your age: "))            #taking age as input from user
city=input("Enter the city name: ")           #taking city name as input from user
college=input("Enter college name: ")         #taking college name as input from user
cgpa=float(input("Enter your marks: "))       #taking cgpa as input from user

print(f"Hey my name is {name},and iam {age} years old.and i am currently staying in {city},studying in {college} college,and i got {cgpa} in my semesters")