import sqlite3

def CreateUser(Name):
	try:
		sqliteConnection = sqlite3.connect('Expenses.db')
		cursor = sqliteConnection.cursor()
		make_user = """INSERT INTO Users (Name) VALUES(?);"""
		cursor.execute(make_user, (Name,))    # change is here
		sqliteConnection.commit()
		print()
		print('User Successfully Created')
		print()
		# cursor.close()
	except sqlite3.Error as error:
			print('Failed to Create User', error)
			print()
	finally:
			if (sqliteConnection):
				sqliteConnection.close()
				print()
				escape = input('Press any key to continue.')


