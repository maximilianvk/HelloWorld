'''
car_test = True
start = 'start'
stop = 'stop'
quit = 'quit'

while car_test == True:
    answer = input('Please choose one of the options: ')
    if answer == start:
        print('You have started the car! Vroom Vroom!')
        break
    elif answer == stop:
        print('You have stopped the car.')
        break
    elif answer == quit:
        print('Thank you playing the car simulations, have a great day!')
        break
    else:
        print('That\'s not a valid answer.')
'''


started = False
command = ''
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car is already started!')
        else:
            started = True
            print('Car started. Ready to go!')
    elif command == 'stop':
        if not started:
            print('Car is already stopped!')
        else:
            started = False
            print('Car Stopped.')
    elif command == 'help':
        print('''
        start - to start the car
        stop - to stop the car
        quit - to exit
        ''')
    else:
        print('That is an invalid answer.')

