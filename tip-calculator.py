print('Welcome to the tip calculator!')
price_of_bill = float(input('What Was The Total Bill? $'))
tip = float(input('How much tip would you like to give? 10, 12, or 15? '))
how_many_peoples_to_split_the_bill = float(input('How many people to split the bill? '))
result = tip/100*price_of_bill+price_of_bill
print(f'Each person should pay: ${round(result,2)/how_many_peoples_to_split_the_bill}')