import random

nums = ['1', '2', '3', '4', '5', '6']
comp_choice = random.choices(nums, k=4)

def score_guess(guess):
    
    assert len(guess) == 4, 'Guess must be 4 nums.'
    assert all([num in nums for num in guess]), 'Invalid guess.'
    
    rightNumRightPlace = 0
    rightNumWrongPlace = 0
    
    if guess == comp_choice:
        return (4, 0)

    remaining_comp_choice = comp_choice.copy()
    remaining_guess = guess.copy()
    
    # Compute rightNumRightPlace first
    for i in range(4):
        if guess[i] == comp_choice[i]:
            rightNumRightPlace += 1
            remaining_comp_choice.remove(comp_choice[i])
            remaining_guess.remove(guess[i])

    # Compute rightNumWrongPlace with the remaining nums
    for i in range(len(remaining_guess)):
        if remaining_guess[i] in remaining_comp_choice:
            rightNumWrongPlace += 1
            remaining_comp_choice.remove(remaining_guess[i])
    
    # print('comp_choice', comp_choice)
    return (rightNumRightPlace, rightNumWrongPlace)

    
def main():
    print('===MASTERMIND===\n')
    num_of_guesses = 0
    while True:
        num_of_guesses += 1
        guess = list(input('Take a guess: '))
        rightNumRightPlace, rightNumWrongPlace = score_guess(guess)
        print(f'Right place: {rightNumRightPlace}, Wrong place: {rightNumWrongPlace}\n')        
        
        if guess == comp_choice:
            break

    print(f'You got it in {num_of_guesses} guesses!')
            
main()
