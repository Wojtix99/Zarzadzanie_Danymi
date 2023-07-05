import sqlite3

def connect():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS equipment
        (name TEXT PRIMARY KEY,
        quantity INTEGER)
        ''')
    conn.commit()
    conn.close()

def add_equipment():
    name = input("Wprowadź nazwę ekwipunku: ")
    quantity = int(input("Wprowadź ilość ekwipunku: "))
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("INSERT INTO equipment VALUES (?, ?)", (name, quantity))
    conn.commit()
    conn.close()
    print("Dodano ekwipunek")

def remove_equipment():
    name = input("Wprowadź nazwę ekwipunku: ")
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("SELECT * FROM equipment WHERE name=?", (name,))
    row = c.fetchone()
    if row:
        quantity = row[1]
        if quantity == 0:
            print("Ekwipunek niedostępny.")
        else:
            c.execute("UPDATE equipment SET quantity=? WHERE name=?", (quantity-1, name))
            conn.commit()
            print("Ekwipunek usunięty.")
    else:
        print("Ekwipunek nie istnieje.")
    conn.close()

def list_inventory():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("SELECT * FROM equipment")
    rows = c.fetchall()
    for row in rows:
        print(f"{row[0]}: {row[1]}")
    conn.close()

def main():
    connect()
    while True:
        print("Wybierz opcje:")
        print("1. Dodaj ekwipunek")
        print("2. Usuń ekwipunek")
        print("3. Lista magazynowa")
        print("4. Wyjście")
        choice = input()
        if choice == '1':
            add_equipment()
        elif choice == '2':
            remove_equipment()
        elif choice == '3':
            list_inventory()
        elif choice == '4':
            break
        else:
            print("Błędna opcja.")

if __name__ == '__main__':
    main()