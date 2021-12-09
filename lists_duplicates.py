numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    '''Locating duplicates within a list'''
    if number not in uniques:
        uniques.append(number)
print(uniques)
