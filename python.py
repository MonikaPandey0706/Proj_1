#Code to detech if the candidate is allowed to vote or not
#LANGUAGE: python 


age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult and eligible to vote")
else:
    print("You are a minor.")

