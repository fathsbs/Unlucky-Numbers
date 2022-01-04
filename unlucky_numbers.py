# show the number and what kind of this number (odd or even)
# for number 4 and 13 just say UNLUCKY!

# first logic 
for number in range(1,21):
    if number == 4 or number == 13:
        print(f'{number} is UNLUCKY!')
    elif number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')

print('\n')

# second logic
for number in range(1,21):
    if number == 4 or number == 13:
        state = 'UNLUCKY!'
    elif number % 2 == 0:
        state = 'even'
    else:
        state = 'odd'
    print(f'{number} is {state}')