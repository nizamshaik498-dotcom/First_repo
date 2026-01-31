#program created using dictionary to store contacts
name=input("Enter name: ")
contacts={"nizam":154251,"althaf":567423,"wahid":654786,"mike":367399}
name=name.lower()
if name in contacts:
    print("The mobile number is: ",contacts[name])
else:
    print("Person not found")