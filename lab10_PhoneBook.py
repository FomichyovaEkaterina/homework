import psycopg2
import csv
def connect():
    return psycopg2.connect(
        host="localhost",
        dbname="Phonebook",
        user="postgres",
        password="I1pop2starpink12345",
        port="5432"
    )

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            phone VARCHAR(15) NOT NULL UNIQUE
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING", row)
    conn.commit()
    cur.close()
    conn.close()

def update_phonebook():
    name = input("Enter the name to update: ")
    phone = input("Enter new phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE PhoneBook SET phone = %s WHERE first_name = %s", (phone, name))
    conn.commit()
    cur.close()
    conn.close()

def query_by_name():
    name = input("Enter name to search: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM PhoneBook WHERE first_name = %s", (name,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def query_all():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM PhoneBook")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def delete_by_value():
    val = input("Enter name or phone to delete: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM PhoneBook WHERE first_name = %s OR phone = %s", (val, val))
    conn.commit()
    cur.close()
    conn.close()

def main():
    create_table()
    while True:
        print("\nMenu:")
        print("1. Insert from console")
        print("2. Insert from CSV")
        print("3. Update phone")
        print("4. Query by name")
        print("5. Query all")
        print("6. Delete by name or phone")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            filename = input("Enter CSV filename: ")
            insert_from_csv(filename)
        elif choice == '3':
            update_phonebook()
        elif choice == '4':
            query_by_name()
        elif choice == '5':
            query_all()
        elif choice == '6':
            delete_by_value()
        elif choice == '0':
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
