import random

def get_comp_num():
    '''Docstring: Ask the user to enter a low and high number.
    Generates a random int between them and return it.
    Inputs: none
    Outputs: comp_num <int>
    '''
    low_num = int(input('Enter a low number. '))
    high_num = int(input('Enter a high number. '))
    comp_num = random.randint(low_num, high_num)
    return comp_num

def get_num_guess():
    guess = int(input('Guess the number. '))
    return guess
        

def main():
    
    comp_num = get_comp_num() 
    num_guesses = 0
    while True:
        guess = get_num_guess()
        num_guesses += 1
        if guess == comp_num:
            print(f'You guessed right my number was {comp_num} it took you {num_guesses} guesses!!!!!')
            break
        if guess < comp_num:
            print('To Low!!!!!')
        if guess > comp_num:
            print('To High!!!!!')


        
    
    
main()





























