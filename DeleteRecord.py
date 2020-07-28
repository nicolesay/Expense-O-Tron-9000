import sqlite3

def DeleteRecord(id, user):
    try:
        sqliteConnection = sqlite3.connect('Expenses.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """DELETE from Expenses WHERE ID = ? AND User = ?"""
        cursor.execute(sql_update_query, (id, user))
        sqliteConnection.commit()
        esc = input("\nRecord deleted successfully\nPress Enter to Continue")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()