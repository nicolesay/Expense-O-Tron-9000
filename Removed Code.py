### Function to Select Transactions Between a Start and End Date ###
def SelectTransactions(date1, date2, user):
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
			time.sleep(.1)
			print('| ' + "{:^6}".format(i[0]) + ' | ' + "{:^15}".format(i[1]) + ' | ' + "{:^25}".format(i[2]) + ' | ' + "{:^15}".format(i[3])
			+ ' | ' + "${:^10.2f}".format(i[4]) + ' | ' + "{:^20}".format(i[5]) + '|')
		print('|--------|-----------------|---------------------------|-----------------|-------------|---------------------|')
		print()
	except sqlite3.Error as error:
		print("Failed to read data from sqlite table", error)
	finally:
		if (sqliteConnection):
			sqliteConnection.close()

			



### Function to Totalize the Selected Transactions, Runs in Conjunction with the SelectTransactions Functuion ###
def SelectTransactionsTotal(date1, date2, user):
	var = 'Expenses'
	var2 = f'SELECT sum(Amount) FROM {var} WHERE cast(Amount as float) < 0 AND Date BETWEEN ? and ? and User = ?'
	try:
		print('Total Expenses & Incomes:\n')
		sqliteConnection = sqlite3.connect('Expenses.db')
		cursor = sqliteConnection.cursor()
		total_query = (var2)
		cursor.execute(total_query, (date1, date2, user))
		total = cursor.fetchmany()
		for item in total:
			print('Total Expenses Are: $' + '{:.2f}'.format(item[0] or 0))

		cursor2 = sqliteConnection.cursor()
		deposits_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) > 0 AND Date BETWEEN ? and ? and User = ?"""
		cursor2.execute(deposits_query, (date1, date2, user))
		deposits = cursor2.fetchmany()
		for item in deposits:
			print('Total Deposits Are: $' + '{:.2f}'.format(item[0] or 0))

		print('\nTotals for Expense Categories:\n')

		cursor3 = sqliteConnection.cursor()
		debts_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) < 0 AND  Category = 'Debts' AND Date BETWEEN ? and ? and User = ?"""
		cursor.execute(debts_query, (date1, date2, user))
		total = cursor.fetchmany()
		for item in total:
			print('Debts: $' + '{:.2f}'.format(item[0] or 0))

		cursor4 = sqliteConnection.cursor()
		entertainment_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) < 0 AND  Category = 'Entertainment' AND Date BETWEEN ? and ? and User = ?"""
		cursor.execute(entertainment_query, (date1, date2, user))
		total = cursor.fetchmany()
		for item in total:
			print('Entertainment: $' + '{:.2f}'.format(item[0] or 0))

		cursor5 = sqliteConnection.cursor()
		food_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) < 0 AND  Category = 'Food' AND Date BETWEEN ? and ? and User = ?"""
		cursor.execute(food_query, (date1, date2, user))
		total = cursor.fetchmany()
		for item in total:
			print('Food: $' + '{:.2f}'.format(item[0] or 0))

		cursor6 = sqliteConnection.cursor()
		healthcare_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) < 0 AND  Category = 'Healthcare' AND Date BETWEEN ? and ? and User = ?"""
		cursor.execute(healthcare_query, (date1, date2, user))
		total = cursor.fetchmany()
		for item in total:
			print('Healthcare: $' + '{:.2f}'.format(item[0] or 0))

		cursor7 = sqliteConnection.cursor()
		home_improvement_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) < 0 AND  Category = 'Home Improvement' AND Date BETWEEN ? and ? and User = ?"""
		cursor.execute(home_improvement_query, (date1, date2, user))
		total = cursor.fetchmany()
		for item in total:
			print('Home Improvement: $' + '{:.2f}'.format(item[0] or 0))

		cursor8 = sqliteConnection.cursor()
		rent_mortgage_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) < 0 AND  Category = 'Rent or Mortgage' AND Date BETWEEN ? and ? and User = ?"""
		cursor.execute(rent_mortgage_query, (date1, date2, user))
		total = cursor.fetchmany()
		for item in total:
			print('Rent & Mortgage: $' + '{:.2f}'.format(item[0] or 0))

		cursor9 = sqliteConnection.cursor()
		saving_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) < 0 AND  Category = 'Saving and Investing' AND Date BETWEEN ? and ? and User = ?"""
		cursor.execute(saving_query, (date1, date2, user))
		total = cursor.fetchmany()
		for item in total:
			print('Saving & Investing: $' + '{:.2f}'.format(item[0] or 0))

		cursor10 = sqliteConnection.cursor()
		transportation_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) < 0 AND  Category = 'transportation' AND Date BETWEEN ? and ? and User = ?"""
		cursor.execute(transportation_query, (date1, date2, user))
		total = cursor.fetchmany()
		for item in total:
			print('Transportation: $' + '{:.2f}'.format(item[0] or 0))

		cursor11 = sqliteConnection.cursor()
		utilities_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) < 0 AND  Category = 'Utilities' AND Date BETWEEN ? and ? and User = ?"""
		cursor.execute(utilities_query, (date1, date2, user))
		total = cursor.fetchmany()
		for item in total:
			print('Utilities: $' + '{:.2f}'.format(item[0] or 0))

		print()
		cont = input('Press Enter to Continue')
	except sqlite3.Error as error:
		print("Failed to read data from sqlite table", error)
	finally:
		if (sqliteConnection):
			sqliteConnection.close()




### FUNCTION TO DELETE RECORD ###
def DeleteRecord(id):
    try:
        sqliteConnection = sqlite3.connect('Expenses.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """DELETE from Expenses where id = ?"""
        cursor.execute(sql_update_query, (id, ))
        sqliteConnection.commit()
        esc = input("\nRecord deleted successfully\nPress Enter to Continue")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()



### From categories.py
		global expense_category
		ExpenseFlag = False
		while ExpenseFlag == False:
			print('Please Choose From the Following Expense Categories:\n')
			for i in expense_nav:
				print(i)
			expense_category = ''
			expense_selection = input('> ')
			if expense_selection == str(1):
				ExpenseFlag = True
				expense_category += 'Debts'
				return(expense_category)
			elif expense_selection == str(2):
				ExpenseFlag = True
				expense_category += 'Entertainment'
				return(expense_category)
			elif expense_selection == str(3):
				ExpenseFlag = True
				expense_category += 'Food'
				return(expense_category)
			elif expense_selection == str(4):
				ExpenseFlag = True
				expense_category += 'Healthcare'
				return(expense_category)
			elif expense_selection == str(5):
				ExpenseFlag = True
				expense_category += 'Home Improvement'
				return(expense_category)
			elif expense_selection == str(6):
				ExpenseFlag = True
				expense_category += 'Rent or Mortgage'
				return(expense_category)
			elif expense_selection == str(7):
				ExpenseFlag = True
				expense_category += 'Saving & Investing'
				return(expense_category)
			elif expense_selection == str(8):
				ExpenseFlag = True
				expense_category += 'Transportation'
				return(expense_category)
			elif expense_selection == str(9):
				ExpenseFlag = True
				expense_category += 'Utilities'
				return(expense_category)
			elif expense_selection != range(1,9):
				print()
				print('Please Make a Valid Selection!')
				cont = input('Press any Key to Continue.')


### Removed from Transaction Totals
	print('Expense & Income Totals:')
	sqliteConnection = sqlite3.connect('Expenses.db')
	cursor = sqliteConnection.cursor()
	total_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) < 0 AND Date BETWEEN ? and ? and User = ?"""
	cursor.execute(total_query, (date1, date2, user))
	total = cursor.fetchmany()
	for item in total:
		print('Total Expenses Are: $' + '{:.2f}'.format(item[0] or 0))

	cursor2 = sqliteConnection.cursor()
	deposits_query = """SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) > 0 AND Date BETWEEN ? and ? and User = ?"""
	cursor2.execute(deposits_query, (date1, date2, user))
	deposits = cursor2.fetchmany()
	for item in deposits:
		print('Total Deposits Are: $' + '{:.2f}'.format(item[0] or 0))
	print()