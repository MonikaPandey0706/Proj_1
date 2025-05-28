#Code to detech if the candidate is allowed to vote or not
#LANGUAGE: python 


age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult and eligible to vote")
else:
    print("You are a minor.")


def check_voting_eligibility(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

# Example usage
user_age = int(input("Enter your age: "))
result = check_voting_eligibility(user_age)
print(result)
i
