weight = float(input('Weight: '))
units = input('(L)bs or (K)g: ')

if units.upper() == 'K':
    print(f"You are {weight*2.2046}  pounds")
elif units.upper() == 'L':
    print(f"You are {weight/2.2046}  pounds")
else:
    print('You have entered wrong unit!!!')


# house_price=1000000
# has_good_credit=False
#
# if has_good_credit:
#     down_payment = house_price*0.1
# else:
#     down_payment = house_price*0.2
#
# print(f"Down payment is: ${down_payment}")



# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink lot of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")