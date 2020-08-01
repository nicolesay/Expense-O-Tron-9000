import sqlite3
import csv

def RecordExport(date1, date2, user):
	try:
		sqliteConnection = sqlite3.connect('Expenses.db')
		cursor = sqliteConnection.cursor()
		sql_select_query = """SELECT * FROM Expenses WHERE Date BETWEEN ? and ? and User = ? ORDER BY Date DESC"""
		cursor.execute(sql_select_query, (date1, date2, user))
		records = cursor.fetchall()
		with open('export.csv', 'w') as file:
			writer = csv.writer(file)
			for i in records:
				writer.writerow(i)
		print('Records Successfully Exported')
		print()
		esc = input('Press Enter to Continue.')
	except sqlite3.Error as error:
		print()
		print("Failed to read data from sqlite table", error)
	finally:
		if (sqliteConnection):
			sqliteConnection.close()