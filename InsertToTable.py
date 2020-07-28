import sqlite3

### Function to Insert Date in to the Database ###
def InsertToTable(Date, Merchant, Description, Amount, Category, User):
	try:
		sqliteConnection = sqlite3.connect('Expenses.db')
		cursor = sqliteConnection.cursor()
		sqlite_insert_with_param = """INSERT INTO Expenses
											(Date, Merchant, Description, Amount, Category, User)
											VALUES (?, ?, ?, ?, ?, ?);"""
		data_tuple = (Date, Merchant, Description, Amount, Category, User)
		cursor.execute(sqlite_insert_with_param, data_tuple)
		sqliteConnection.commit()
		print()
		print('Data Successfully Inserted in to Table.')
		print()
		# cursor.close()
	except sqlite3.Error as error:
			print('Failed to Insert Data in to Table.', error)
			print()
	finally:
			if (sqliteConnection):
				sqliteConnection.close()
				print()
				escape = input('Press any key to continue.')