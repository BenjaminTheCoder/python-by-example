def reverseString(msg):
    return msg[::-1]

def main2():
    reversedMsg = reverseString(input('enter a message. '))
    for c in reversedMsg:
        print(c)

def main():
    msg = input('enter a message. ')
    for i in range(len(msg)-1,-1,-1):
        print(msg[i])
    

main2()
