import sqlite3
sqliteConnection = sqlite3.connect('Expenses.db')
sqliteConnection2 = sqlite3.connect('Expenses.db')
# cursor = sqliteConnection.cursor()
# categories_query = 'SELECT * FROM ExpenseCategories ORDER BY Name ASC'
# cursor.execute(categories_query)
# categories = cursor.fetchall()
# cat = []
# for i in categories:
#     cat.append(i)


# sqliteConnection2 = sqlite3.connect('Expenses.db')
# cursor2 = sqliteConnection.cursor()
# categories_query2 = 'SELECT * FROM IncomeCategories ORDER BY Name ASC'
# cursor2.execute(categories_query)
# categories2 = cursor2.fetchall()
# cat2 = []
# for i in categories2:
#     cat2.append(i)

class CategoryTotals():

	def IncomeTotals(cat, date1, date2, user):
		import_query2 = f'SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) > 0 AND  Category = "{cat}" AND Date BETWEEN ? and ? and User = ?'
		cursor2 = sqliteConnection2.cursor()
		query2 = import_query2
		cursor2.execute(query2, (date1, date2, user))
		total2 = cursor2.fetchmany()
		for item in total2:
		    print(f'{cat}: $' + '{:.2f}'.format(item[0] or 0))

	def IncomeTotalAmount(date1, date2, user):
		cursor2 = sqliteConnection.cursor()
		deposits_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) > 0 AND Date BETWEEN ? and ? and User = ?"""
		cursor2.execute(deposits_query, (date1, date2, user))
		deposits = cursor2.fetchmany()
		for item in deposits:
			print('Total Income Items Are: $' + '{:.2f}'.format(item[0] or 0))


	def ExpenseTotals(cat, date1, date2, user):
		import_query = f'SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) < 0 AND  Category = "{cat}" AND Date BETWEEN ? and ? and User = ?'
		cursor = sqliteConnection.cursor()
		query = import_query
		cursor.execute(query, (date1, date2, user))
		total = cursor.fetchmany()
		for item in total:
		    print(f'{cat}: $' + '{:.2f}'.format(item[0] or 0))


	def ExpenseTotalAmount(date1, date2, user):
		cursor = sqliteConnection.cursor()
		total_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) < 0 AND Date BETWEEN ? and ? and User = ?"""
		cursor.execute(total_query, (date1, date2, user))
		total = cursor.fetchmany()
		for item in total:
			print('Total Expenses Are: $' + '{:.2f}'.format(item[0] or 0))










