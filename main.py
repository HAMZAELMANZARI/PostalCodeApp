import sqlite3

INPUT_MENU = """Welcome in Postal Code App\n
1. Add Postal Code.\n
2. View Postal Code.\n
3. Update Postal code.\n
4. Delete Postal code.\n
5. Exit.
\n"""

db = sqlite3.connect("database/postal_code.db")

cur = db.cursor()

# cur.execute("CREATE TABLE postal_code(user_id INTEGER, city TEXT, postal_code INTEGER)")

choose = int(input(f"{INPUT_MENU}Choose one numbers: "))


def add_postal_code():

    """Added postal code a db"""

    user_id = input("Enter User id: ").capitalize().strip()

    if len(user_id) < 1:

        print("Enter argument")

        return

    city = input("Enter City Name: ").capitalize().strip()

    postal_num = input("Enter Postal Code:").capitalize().strip()

    cur.execute(f"INSERT INTO postal_code VALUES (?,?,?)",(user_id,city,postal_num))

    db.commit()

    print("Added is Successfly.\n")

    exit_and_close()


def veiw_postal_code():

    """View all a db"""

    for item in cur.execute("SELECT * FROM postal_code"):

        print(f"User id: {item[0]} | City name: {item[1]} | Postal Code: {item[2]}")

def update_postal_code():

    """Update a database rows"""

    user_id = input("Enter user_id: ").strip()

    cur.execute("SELECT user_id FROM postal_code WHERE user_id = ?",(user_id))

    result = cur.fetchone()

    if result:

        city = input("Enter new city: ").capitalize().strip()

        postal_number = input("Enter new postal number: ").capitalize().strip()

        cur.execute("UPDATE postal_code SET city = ?, postal_code = ? WHERE user_id = ?", (city, postal_number, user_id))

        db.commit()

        print("Update is Successful.\n")

        exit_and_close()

    else:

        print("User ID not found. Not Updating.\n")

        exit_and_close()

def delete_postal_code():

    """Deleted a db in rows"""

    user_id = input("Enter user_id: ").strip()

    cur.execute("SELECT user_id FROM postal_code WHERE user_id = ?",(user_id))

    result = cur.fetchone()

    if result:

        cur.execute("DELETE FROM postal_code WHERE user_id= ?",(user_id,))
        
        db.commit()

        print("Deleted a Successfuly.\n")

        exit_and_close()
    
    else:

        print("User ID not found. Not Deleted !\n")

        exit_and_close()

def exit_and_close():

    """Closed DB and existing app"""

    db.close()

    print("Existing...")

def run():

    """Run meun choose"""

    if choose == 1 :

        add_postal_code()

    elif choose == 2:

        veiw_postal_code()

    elif choose == 3:

        update_postal_code()
    
    elif choose == 4:

        delete_postal_code()

    elif choose == 5:

        exit_and_close()

    else:

        print("Invalid Not Found!")

if __name__ == "__main__":

    run()





    

