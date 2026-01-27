#program created using string methods and converts the user input to title case and counts how many vowels are in it.

prompt=input("Enter any sentence: ")                        #takes input from user
print("Your Input Is: ",prompt)
print("Coverted to title case: ",prompt.title())            #coverts to title case
vowels=(prompt.lower().count('a')+                          #counts vowels in the input
        prompt.lower().count('e')+
        prompt.lower().count('i')+
        prompt.lower().count('o')+
        prompt.lower().count('u'))
print("Vowels Found: ",vowels)                              #prints number of vowels found