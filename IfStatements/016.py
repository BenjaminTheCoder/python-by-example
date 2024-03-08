rain = input('Is it raining? ').lower()

if rain == 'yes':
    wind = input('Is it windy? ').lower()
    if wind == 'yes':
        print('It is to windy for an umbrella.')
    else:   
        print('Take a umbrella')
else:
    print('Have a nice day.')





