import random
response = 'y'
while response == 'y':
    no = random.randint(1,6)
    if no == 1:
        print('-----')
        print()
        print('  0  ')
        print()
        print('-----')
    
    if no == 2:
        print('-----')
        print()
        print('  10  ')
        print()
        print('-----')

    if no == 3:
        print('-----')
        print()
        print('  100  ')
        print()
        print('-----')

    if no == 4:
        print('-----')
        print()
        print('  1000  ')
        print()
        print('-----')

    if no == 5:
        print('-----')
        print()
        print('  10000  ')
        print()
        print('-----')

    if no == 6:
        print('-----')
        print()
        print('  1000000  ')
        print()
        print('-----')

    response = input('Press y to continue and n to exit :- ')