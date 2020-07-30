import sqlite3
expense_category = ''
income_category = ''
expense_selection = ''
income_selection = ''

# expense_nav = ['1 - Debts', '2 - Entertainment', '3 - Food','4 - Healthcare', '5 - Home Improvement', '6 - Rent or Mortgage', '7 - Saving and Investing', '8 - Transportation', '9 - Utilities']
income_nav = ['1 - Salary', '2 - Other Income', '3 - Refunds', '4 - Balance Adjustment']

class Categories:
	### This is a class that lets the user select the expense or income category they want to use
	
	def ExpenseSelection():
		global expense_selection
		sqliteConnection = sqlite3.connect('Expenses.db')
		cursor = sqliteConnection.cursor()
		cursor.execute('SELECT ID, Name FROM ExpenseCategories')
		userdict = dict(cursor.fetchall())
		print()
		for key, value in userdict.items():
			print(key, value)
		print()
		while True:
			try:
				userselect = int(input('Please Choose a Category Number:\n> '))
				if userselect in userdict.keys():
					expense_selection += userdict.get(userselect)
				elif userselect not in userdict.keys():
					print('Invalid User Selected, Please Try Again')
					continue
				return expense_selection
			except ValueError:
				print('Must be a Number!')


	def IncomeSelection():
		global income_selection
		sqliteConnection = sqlite3.connect('Expenses.db')
		cursor = sqliteConnection.cursor()
		cursor.execute('SELECT ID, Name FROM IncomeCategories')
		userdict = dict(cursor.fetchall())
		print()
		for key, value in userdict.items():
			print(key, value)
		print()
		while True:
			try:
				userselect = int(input('Please Choose a Category Number:\n> '))
				if userselect in userdict.keys():
					income_selection += userdict.get(userselect)
				elif userselect not in userdict.keys():
					print('Invalid User Selected, Please Try Again')
					continue
				return income_selection
			except ValueError:
				print('Must be a Number!')



	# def IncomeSelection():
	# 	global income_category
	# 	IncomeFlag = False
	# 	while IncomeFlag == False:
	# 		print('Please Choose From the Following Income Categories:\n')
	# 		for i in income_nav:
	# 			print(i)
	# 		income_category = ''
	# 		income_selection = input('> ')
	# 		if income_selection == str(1):
	# 			IncomeFlag = True
	# 			income_category += 'Salary'
	# 			return income_category
	# 		elif income_selection == str(2):
	# 			IncomeFlag = True
	# 			income_category += 'Other Income'
	# 			return income_category
	# 		elif income_selection == str(3):
	# 			IncomeFlag = True
	# 			income_category += 'Refunds'
	# 			return income_category
	# 		elif income_selection == str(4):
	# 			IncomeFlag = True
	# 			income_category += 'Balance Adjustment'
	# 			return income_category
	# 			print(income_category)
	# 		elif income_selection != range(1,4):
	# 			print()
	# 			print('Please Make a Valid Selection!')
	# 			cont = input('Press any Key to Continue.')





