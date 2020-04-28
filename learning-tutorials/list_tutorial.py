# MIN_DRIVING_AGE = 18
#
#
# def allowed_driving(name, age):
#     """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
#        checking the passed in age against the MIN_DRIVING_AGE constant"""
#     is_allowed = 'is allowed' if age >= MIN_DRIVING_AGE else 'is not allowed'
#     print(f'{name} {is_allowed} to drive')
#
# allowed_driving('Hemanth',16)
#

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

str = ''
for car in cars:
    if car == 'Jeep':
        for value1 in cars[car]:
            str = str + ',' + value1
print(str[1:])


print('********************')

resultlist = list();

for car in cars.values():
    resultlist.append(car[0])

print(resultlist)

print('********************')

searchstring='CO'
finallist = list()

for mapValue in cars.values():
    for item in mapValue:
        if item.upper().__contains__(searchstring.upper()):
            finallist.append(item)

finallist.sort()
print(finallist)

print('********************')

for key in sorted(cars.keys()):
    cars[key].sort()
    print("'%s': %s" % (key, cars[key]))



