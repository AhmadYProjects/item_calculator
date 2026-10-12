# setup_db.py
import sqlite3

ie_data = (3031,'Infinity Edge', 3500, 75,25,30)
def init_database():
    # 1. Connects to the database file. If it doesn't exist, Python creates it!
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # 2. Define your table structure matching your snake_case stats
    cursor.execute("""Select * FROM items WHERE name = 'Infinity Edge';
                   """)
    item = cursor.fetchone()
    print(item)

    # 3. Commit changes and close the connection safely
    conn.commit()
    conn.close()
    print("Query Executed Successfully!")


if __name__ == "__main__":
    init_database()