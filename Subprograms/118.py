def get_num():
    num = int(input('enter a number. '))
    return num


def num_count(num):
    for i in range(1, num+1):
        print(i)

def main():
    num = get_num() 
    num_count(num)
    
    
    
main()





























