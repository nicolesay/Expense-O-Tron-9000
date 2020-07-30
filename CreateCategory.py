import sqlite3


class CreateCategory:
	### Function to Insert Categories in to the Database ###
	def ExpenseCategory(Name):
		try:
			sqliteConnection = sqlite3.connect('Expenses.db')
			cursor = sqliteConnection.cursor()
			sqlite_insert_with_param = """INSERT INTO ExpenseCategories
												(Name)
												VALUES (?);"""
			cursor.execute(sqlite_insert_with_param, (Name,))
			sqliteConnection.commit()
			print()
			print('New Expense Category Successfully Created.')
			print()
			cursor.close()
		except sqlite3.Error as error:
				print('Failed to Create New Category.', error)
				print()
		finally:
				if (sqliteConnection):
					sqliteConnection.close()
					print()
					escape = input('Press any key to continue.')

	def IncomeCategory(Name):
		try:
			sqliteConnection = sqlite3.connect('Expenses.db')
			cursor = sqliteConnection.cursor()
			sqlite_insert_with_param = """INSERT INTO IncomeCategories
												(Name)
												VALUES (?);"""
			cursor.execute(sqlite_insert_with_param, (Name,))
			sqliteConnection.commit()
			print()
			print('New Income Category Successfully Created.')
			print()
			cursor.close()
		except sqlite3.Error as error:
				print('Failed to Create New Category.', error)
				print()
		finally:
				if (sqliteConnection):
					sqliteConnection.close()
					print()
					escape = input('Press any key to continue.')