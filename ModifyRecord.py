import sqlite3

def ModifyRecord(Date, Merchant, Description, Amount, Category, ID, User):
	try:
		sqliteConnection = sqlite3.connect('Expenses.db')
		cursor = sqliteConnection.cursor()
		sql_update_query = """Update Expenses Set Date = ?, Merchant = ?, Description = ?, Amount = ?, Category = ? WHERE ID = ? AND User = ?"""
		data = (Date, Merchant, Description, Amount, Category, ID, User)
		cursor.execute(sql_update_query, data)
		sqliteConnection.commit()
		print()
		print("Record Updated successfully")
		print()
		esc = input('Press Enter to Continue')
		cursor.close()

	except sqlite3.Error as error:
		print("Failed to update sqlite table", error)
	finally:
		if (sqliteConnection):
			sqliteConnection.close()
			print("The sqlite connection is closed")