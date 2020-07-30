import sqlite3

# expense_nav = ['1 - Debts', '2 - Entertainment', '3 - Food','4 - Healthcare', '5 - Home Improvement', '6 - Rent or Mortgage', '7 - Saving and Investing', '8 - Transportation', '9 - Utilities']
# income_nav = ['1 - Salary', '2 - Other Income', '3 - Refunds', '4 - Balance Adjustment']
# expenses2 = ['Debts', 'Entertainment']
expense_selection = ''

def ExpenseNav():
	global expense_selection
	sqliteConnection = sqlite3.connect('Expenses.db')
	cursor = sqliteConnection.cursor()
	cursor.execute('SELECT ID, Name FROM Categories')
	userdict = dict(cursor.fetchall())
	print()
	for key, value in userdict.items():
		print(key, value)
	print()
	while True:
		try:
			userselect = int(input('Please Choose a Category\n> '))
			if userselect in userdict.keys():
				expense_selection += userdict.get(userselect)
			elif userselect not in userdict.keys():
				print('Invalid User Selected, Please Try Again')
				continue
			return expense_selection
		except ValueError:
			print('Must be a Number!')

ExpenseNav()
print('Your Choice is ' + str(expense_selection))