# Ask the user to enter the state they live in. Display the first two letters of the state in uppercase.
# Example: Washington WA


def main2():
    print(input('What state do you live in? ')[:2].upper())

def main():
    state = input('What state do you live in?. ')
    sliced = state[:2]
    response = sliced.upper()
    print(response)

    
main2()
