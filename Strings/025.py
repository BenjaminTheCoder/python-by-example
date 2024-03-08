firstname = input('What is your first name? ')
if len(firstname) < 5:
    lastname = input('What is your last name? ')
    answer = (firstname+lastname).upper()
    print(f'{answer}')
else:
    print(f'Your name is {firstname.lower()}.') 

# Pseudocode
# Ask the user for their first name and store it in firstname.
# If the length of the first name is under 5 characters:
#   Ask the user for their last name and store it in lastname.
#   Concatenate the first and last name and upper case it and store it in answer.
#   Print the answer.
# Otherwise:
#   Print the first name in lower case.
