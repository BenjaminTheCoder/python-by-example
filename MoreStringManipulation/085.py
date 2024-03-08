# aeiou

def isVowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u']


def main2():
    name = input('Enter your name please. ').lower()
    vowels = filter(isVowel, list(name))
    print(f'Their are {len(list(vowels))} vowels in your name.')

def main():
    num = 0
    name = input('Enter your name please. ').lower()
    for letter in name:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            num += 1
    print(f'Their are {num} vowels in your name.')


main()
