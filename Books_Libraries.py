import sqlite3 as sql

# Function of the application

class DatabaseManage(object):

    def __init__(self):
        global dbcon
        try:
            dbcon = sql.connect('book.db')
            with dbcon:
                cur = dbcon.cursor()
                cur.execute('Create a table if not exists book(Id INTERGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)')
        except Exception:
            print("Unable to create a DataBase!\n")

    # CREATE DATA
    def insert_data(self, data):
        try:
            with dbcon:
                cur = dbcon.cursor()
                cur.execute(
                    'INSERT INTO BOOK(name, description, price, is_private) '
                    'VALUES (?,?,?,?)', data
                )
            return True
        except Exception:
            return False

    # READ DATA
    def fetch_data(self):
        try:
            with dbcon:
                cur = dbcon.cursor()
                cur.execute('SELECT * FROM courses')
                return cur.fetchall()
        except Exception:
            return False

    # DELETE DATA
    def delete_data(self, Id):
        try:
            with dbcon:
                cur = dbcon.cursor()
                sequel = 'DELETE FROM book WHERE id = ?'
                cur.execute(sequel, [Id])
                return True
        except Exception:
            return False


# User Interface for user

def main():
    print(":: DIGITAL BOOKS LIBRARY ::")
    print("#" * 50)
    print("\n")

    db = DatabaseManage()

    print(":: User Instruction ::")
    print('1. Insert a New Book')
    print('2. Display List of all Books ')
    print('3. Delete a Book(NEED ID)')
    print("\n")

    choice = input('\n Enter  choice: ')

    if choice == "1":
        name = input("\n Enter Book Name: ")
        description = input("\n Enter Book Description: ")
        price = input("\n Enter Book Price: ")
        private = input("\n Is this book is private(0/1): ")

        if db.insert_data([name, description, price, private]):
            print("Book inserted successfully")
        else:
            print("Something goes wrong !")

    elif choice == "2":
        print('\n:: Books List ::')

        for index, item in enumerate(db.fetch_data()):
            print('\n SL No:'+str(index+1))
            print('Book Id: '+str(item[0]))
            print('Book Name: '+str(item[1]))
            print('Book Description: '+ str(item[2]))
            print('Book Price: ' + str(item[3]))
            private = 'Yes' if item[4] else 'No'
            print('Is Private: '+private)

    elif choice == "3":
        record_id = input("Enter Book Id: ")

        if db.delete_data(record_id):
            print("Successfully Deleted")
        else:
            print('Something Goes Wrong')

    else:
        print('\n Worng Choice')


if __name__ == '__main__':
    main()









