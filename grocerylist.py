def grocery_list(grocerylist):
    print(f'Here is the current grocery list: {grocerylist}')


def add_to_list():

    add_item = input('What would you like to add: ')

    grocery_list = grocerylist.append(add_item)

    return grocery_list

def add_more():

    choice = 'wrong'

    while choice not in ['Y','N']:
        choice = input('Would you like to add more Y or N? ')

        if choice not in ['Y','N']:
            print('Invalid Input')
    
    if choice == 'Y':
        return True
    else:
        return False
    

expandlist = True
grocerylist = ['apple','pork','eggs']

while expandlist:
    grocery_list(grocerylist)

    add_to_list()

    grocery_list(grocerylist)

    expandlist = add_more()