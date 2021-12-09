# To greet users
def greet_user(first_name,last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome Aboard')



print("Start")
greet_user(input('Please input Name: '), input('Please input last name: '))
# Key words such as last_name CANNOT be the first parameter, and then follow thru with a positional arguement
greet_user('John', last_name = 'Smith')
print('Finish')


