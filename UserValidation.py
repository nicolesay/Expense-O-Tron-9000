import sqlite3
current_user = ''
user_selection = ''

def CurrentUser():
    global user_selection
    global current_user
    sqliteConnection = sqlite3.connect('Expenses.db')
    cursor = sqliteConnection.cursor()
    user_select = 'SELECT * FROM Users'
    cursor.execute(user_select)
    users = cursor.fetchall()
    user_numbers = []
    user_list = []
    ### Appends the user ID# (IE: 1, 2, etc) to the list user_numbers
    for i in users:
        user_numbers.append(i[0])
    print(user_numbers)
    ### Appends the user ID & name to the list user_list
    for i in users:
        user_list.append(i)
    print('Current User List is: ')
    print()
    ### Prints the user ID + the User name, IE: "1 - Username"
    for i in user_list:
        print(str(i[0]) + ' - ' + str(i[1]))
    ### Ensuring the selection is a number and not another character
    while True:
        try:
            user_selection == int(input('Select User Number > '))
            print(type(user_selection))
            break
        except ValueError:
            print('Must be a Number!')
            continue
    for i in user_list:
        if user_selection in user_numbers:
            print('True')
        if user_selection == int(i[0]):
            current_user += str(i[1])
        print(current_user)
        return current_user


CurrentUser()

