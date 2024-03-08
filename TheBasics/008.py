bill = float(input('What is the price of the bill? '))
people = int(input('How many ate? '))
payment = bill / people 
print('Each one of you must pay ', round(payment,2), 'dollars.')
