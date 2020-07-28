import sqlite3

current_user = ''

def CurrentUser():
	global current_user
	sqliteConnection = sqlite3.connect('Expenses.db')
	cursor = sqliteConnection.cursor()
	cursor.execute('SELECT ID, Name FROM Users')
	userdict = dict(cursor.fetchall())
	print()
	for key, value in userdict.items():
		print(key, ' - ', value)
	print()
	while True:
		try:
			userselect = int(input('Enter User ID\n> '))
			if userselect in userdict.keys():
				current_user += userdict.get(userselect)
			elif userselect not in userdict.keys():
				print('Invalid User Selected, Please Try Again')
				continue
			return current_user
		except ValueError:
			print('Must be a Number!')