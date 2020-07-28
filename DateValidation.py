import datetime

def DateValidation():
	while True:
		try:
			date = input('Enter Date in MM/DD/YYYY Format > ')
			datetime.datetime.strptime(date, '%m/%d/%Y')
			date = str(date)
			return date
		except ValueError:
			print('Incorrect Date Format, Should be MM/DD/YYYY')
			continue