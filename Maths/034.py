shape = int(input('1) Square, 2) Triangle '))
if shape == 1:
    side = int(input('Enter the length of 1 side. '))
    area = side**2
    print(f'area of a square: {area}')
elif shape == 2: 
    base = int(input('What is the length of the base. '))
    height = int(input('What is the length of the height. '))
    area2 = (base * height) / 2.0
    print(f'area of a triangle: {area2}')
else:
    print('Will not understand')

 





