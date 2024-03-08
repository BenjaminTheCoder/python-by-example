word = input('Enter a word ').lower()
firstletter = word[0]
if firstletter in ['a', 'e', 'i', 'o', 'u']:
    print(word + 'way')
else:
    rest = word[1:]
    print(rest + firstletter + 'ay')
    
         



##ask the user for a word.
##if the first letter is a consanent:
##    add the first letter to the end of the word and add ay to the end of the word.
##    display the result
##otherwise:
##    add way to the end of the word.
##    display the word like this.



