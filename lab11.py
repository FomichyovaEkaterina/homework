import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        dbname="Phonebook",
        user="postgres",
        password="I1pop2starpink12345",
        port="5432"
    )

def search_by_pattern():
    pattern = input("Enter pattern to search: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def insert_or_update():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_bulk():
    names = input("Enter names separated by commas: ").split(',')
    phones = input("Enter phones separated by commas: ").split(',')
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_bulk_users(%s, %s)", (names, phones))
    conn.commit()
    cur.close()
    conn.close()

def get_users():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_users_by_page(%s, %s)", (limit, offset))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def get_all_users():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM PhoneBook ORDER BY id")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def delete_user():
    val = input("Enter name or phone to delete: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_user(%s)", (val,))
    conn.commit()
    cur.close()
    conn.close()

def main():
    while True:
        print("""
Menu:
1. Insert or update user
2. Insert bulk users
3. Search by pattern
4. Get users (pagination)
5. Delete user
6. Show all users
0. Exit
""")
        choice = input("Choose an option: ")

        if choice == '1':
            insert_or_update()
        elif choice == '2':
            insert_bulk()
        elif choice == '3':
            search_by_pattern()
        elif choice == '4':
            get_users()
        elif choice == '5':
            delete_user()
        elif choice == '6':
            get_all_users()
        elif choice == '0':
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
