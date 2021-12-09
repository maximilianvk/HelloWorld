# Dicitionary

customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True

}
#If you want to input another key word within a dictionary, you can do it like below.

customer['birthday'] = 'Jan 1 1980'
print(customer['birthday'])

# Problem to solve

phone = input('Phone: ')
digit_mapping = {
    "1":"One ",
    "2":"Two ",
    "3":"Three ",
    "4":"Four "
}
output = ''
for ch in phone:
    output += digit_mapping.get(ch, '!') + " "
print(output)
