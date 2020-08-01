import sqlite3

def TransactionTable(date1, date2, user):
	try:
		sqliteConnection = sqlite3.connect('Expenses.db')
		cursor = sqliteConnection.cursor()
		sql_select_query = """SELECT * FROM Expenses WHERE Date BETWEEN ? and ? and User = ? ORDER BY Date DESC"""
		cursor.execute(sql_select_query, (date1, date2, user))
		records = cursor.fetchall()
		print()
		print('|--------|-----------------|---------------------------|-----------------|-------------|---------------------|')
		print('|   ID   |      Date       |          Merchant         |   Description   |    Amount   |       Category      |')
		print('|--------|-----------------|---------------------------|-----------------|-------------|---------------------|')
		records_list = []
		for i in records:
			records_list.append(i)
		for i in records_list:
			print('| ' + "{:^6}".format(i[0]) + ' | ' + "{:^15}".format(i[1]) + ' | ' + "{:^25}".format(i[2]) + ' | ' + "{:^15}".format(i[3])
			+ ' | ' + "${:^10.2f}".format(i[4]) + ' | ' + "{:^20}".format(i[5]) + '|')
		print('|--------|-----------------|---------------------------|-----------------|-------------|---------------------|')
		print()

	except sqlite3.Error as error:
		print("Failed to read data from sqlite table", error)
	finally:
		if (sqliteConnection):
			sqliteConnection.close()

