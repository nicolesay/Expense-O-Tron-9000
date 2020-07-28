import sqlite3
sqliteConnection = sqlite3.connect('Expenses.db')
cursor = sqliteConnection.cursor()
categories_query = 'SELECT * FROM ExpenseCategories ORDER BY Name ASC'
cursor.execute(categories_query)
categories = cursor.fetchall()
cat = []
for i in categories:
    cat.append(i)

def CategoryTotals(cat, date1, date2, user):
    import_query = f'SELECT sum(Amount) FROM Expenses WHERE cast(Amount as float) < 0 AND  Category = "{cat}" AND Date BETWEEN ? and ? and User = ?'
    cursor = sqliteConnection.cursor()
    query = import_query
    cursor.execute(query, (date1, date2, user))
    total = cursor.fetchmany()
    for item in total:
        print(f'{cat}: $' + '{:.2f}'.format(item[0] or 0))










