### Imports
import sqlite3
from DateValidation import *
from IsNumber import *
from Categories import *
from CurrentUser import *
from CreateUser import *
from CategoryTotals import *
from TransactionTable import *
from InsertToTable import *
from ModifyRecord import *
from DeleteRecord import *
from CreateCategory import *


### Initialize Main SQLite Connection ###
sqliteConnection = sqlite3.connect('Expenses.db')
cursor = sqliteConnection.cursor()

### List That is Printed out for the User Navigation ###
navigation = ['1 - Enter a Transaction', '2 - Display Transactions', '3 - Modify a Transaction', '4 - Delete a Transaction', '5 - Options', '6 - Quit']

print()
print('|------------------------------------------------------------------------------------------------------------|')
print('|                                                                                                            |')
print('|                          WELCOME TO THE EXPENSE-O-TRON 9000 ACCOUNTING SYSTEM                              |')
print('|                                                                                                            |')
print('|------------------------------------------------------------------------------------------------------------|')
print()
cont = input('Press any Key to Continue...')

current_user = CurrentUser()
print('Current User is ' + str(current_user))

### Flag That Runs the For Loop ###
flag = False

while flag == False:
	print()
	for i in navigation:
		print(i)
	ask = input('> ')

	## Main Menu - Create Transaction 
	if ask == str(1):
		selectionnav1 = False
		while selectionnav1 == False:
			print()
			selection1 = input('Is this an Expense or Deposit? \n1 - Expense\n2 - Income\n3 - Return to Previous Menu\n> ')
			### Menu 1 Sub-Menu 1 - Input Expense
			if selection1 == str(1):
				selectionnav1 == True
				print('Please Input Transaction Information:')
				print()
				date = DateValidation()
				i_merchant = input('Enter Merchant Name > ')
				i_description = input('Enter Transaction Description > ')
				i_amount = IsNumber()
				### Function to Load the Selection of Expense Categories
				expense_selection = Categories.ExpenseSelection()
				InsertToTable(date, i_merchant, i_description, (i_amount * -1), expense_selection, current_user)

			### Menu 1 Sub-Menu 2 - Input Income
			elif selection1 == str(2):
				selectionnav1 == True
				print('Please Input Transaction Information:')
				print()
				date = DateValidation()
				i_merchant = input('Enter Merchant Name > ')
				i_description = input('Enter Transaction Description > ')
				i_amount = IsNumber()
				### Function to Load the Selection of Income Categories
				income_selection = Categories.IncomeSelection()
				InsertToTable(date, i_merchant, i_description, i_amount, income_selection, current_user)
			elif selection1 == str(3):
				break
			else:
				break
		cursor.close()
	elif ask == str('2'):
		print()
		start_date = DateValidation()
		end_date = DateValidation()
		TransactionTable(start_date, end_date, current_user)

		sqliteConnection = sqlite3.connect('Expenses.db')
		inc_cursor = sqliteConnection.cursor()
		inc_categories_query = 'SELECT * FROM IncomeCategories'
		inc_cursor.execute(inc_categories_query)
		inc_categories = inc_cursor.fetchall()
		inc_cat = []
		for i in inc_categories:
			inc_cat.append(i)
		print('Income Category Totals:')
		for i in inc_cat:
			CategoryTotals.IncomeTotals(i[0], start_date, end_date, current_user)
		CategoryTotals.IncomeTotalAmount(start_date, end_date, current_user)
		cursor.close()

		print()
		sqliteConnection = sqlite3.connect('Expenses.db')
		exp_cursor = sqliteConnection.cursor()
		exp_categories_query = 'SELECT * FROM ExpenseCategories'
		exp_cursor.execute(exp_categories_query)
		exp_categories = exp_cursor.fetchall()
		exp_cat = []
		for i in exp_categories:
			exp_cat.append(i)

		print('Expense Category Totals:')
		for i in exp_cat:
			CategoryTotals.ExpenseTotals(i[0], start_date, end_date, current_user)
		CategoryTotals.ExpenseTotalAmount(start_date, end_date, current_user)
		cursor.close()

	### Main Menu - Modify a Transaction
	elif ask == str('3'):
		print()
		selectionnav3 = False
		while selectionnav3 == False:
			selection3 = input('Is this an Expense or Deposit? \n1 - Expense\n2 - Deposit\n3 - Return to Previous Menu\n> ')

			### Menu 2 Sub-Menu 1 - Modify Expense Transaction
			if selection3 == str(1):
				selectionnav3 == True
				print('Please Input Transaction Information:')
				print()
				i_ID = input('Enter Transaction ID > ')
				date = DateValidation()
				i_merchant = input('Enter Merchant Name > ')
				i_description = input('Enter Transaction Description > ')
				i_amount = IsNumber()
				### Function to Load the Selection of Expense Categories
				expense_selection = Categories.ExpenseSelection()
				ModifyRecord(date, i_merchant, i_description, (i_amount * -1), expense_selection, i_ID, current_user)

			### Menu 2 Sub-Menu 1 - Modify Income Transaction
			elif selection3 == str(2):
				selectionnav3 == True
				print('Please Input Transaction Information:')
				print()
				i_ID = input('Enter Transaction ID > ')
				date = DateValidation()
				i_merchant = input('Enter Merchant Name > ')
				i_description = input('Enter Transaction Description > ')
				i_amount = IsNumber()
				### Function to Load the Selection of Income Categories
				income_selection = Categories.IncomeSelection()
				ModifyRecord(date, i_merchant, i_description, i_amount, income_selection, i_ID, current_user)
			elif selection3 == str(3):
				break
			else:
				break
	### Main Menu - Delete Transaction
	elif ask == str('4'):
		print()
		i_ID = input('Input the ID of the Transaction to be Deleted\n>')
		DeleteRecord(i_ID, current_user)

	### Main Menu - Options
	elif ask == str('5'):
		print()
		selectionnav5 = False
		while selectionnav5 == False:
			selection5 = input('1 - Create New User\n2 - Switch Users\n3 - Create New Expense Category\n4 - Create New Income Category\n5 - Return to Previous Menu\n> ')
			if selection5 == str(1):
				selectionnav5 = True
				new_user = input('Input Desired Username > ')
				CreateUser(new_user)
			elif selection5 == str(2):
				selectionnav5 = True
				current_user = ''
				CurrentUser()
			elif selection5 == str(3):
				new_category = input('Please Input Name of New Expense Category > ')
				CreateCategory.ExpenseCategory(new_category)
			elif selection5 == str(4):
				new_category = input('Please Input Name of New Income Category > ')
				CreateCategory.IncomeCategory(new_category)
			elif selection5 == str(5):
				break
			else:
				break
		print('Current User is: ' + str(current_user))

	### Main Menu - Quit
	elif ask == str('6') or 'goodbye':
		print('Goodbye!')
		flag = True
