# setup_db.py
import sqlite3


def init_database():
    # 1. Connects to the database file. If it doesn't exist, Python creates it!
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # 2. Define your table structure matching your snake_case stats
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS items
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       name
                       TEXT
                       NOT
                       NULL,
                       gold
                       INTEGER
                       DEFAULT
                       0,
                       attack_damage
                       INTEGER
                       DEFAULT
                       0,
                       attack_speed
                       INTEGER
                       DEFAULT
                       0,
                       critical_strike_chance
                       INTEGER
                       DEFAULT
                       0,
                       life_steal
                       INTEGER
                       DEFAULT
                       0,
                       armor_penetration
                       INTEGER
                       DEFAULT
                       0,
                       lethality
                       INTEGER
                       DEFAULT
                       0,
                       ability_power
                       INTEGER
                       DEFAULT
                       0,
                       ability_haste
                       INTEGER
                       DEFAULT
                       0,
                       mana
                       INTEGER
                       DEFAULT
                       0,
                       mana_regeneration
                       INTEGER
                       DEFAULT
                       0,
                       heal_and_shield_power
                       INTEGER
                       DEFAULT
                       0,
                       omnivamp
                       INTEGER
                       DEFAULT
                       0,
                       flat_magic_penetration
                       INTEGER
                       DEFAULT
                       0,
                       percent_magic_penetration
                       INTEGER
                       DEFAULT
                       0,
                       health
                       INTEGER
                       DEFAULT
                       0,
                       health_regeneration
                       INTEGER
                       DEFAULT
                       0,
                       armor
                       INTEGER
                       DEFAULT
                       0,
                       magic_resistance
                       INTEGER
                       DEFAULT
                       0,
                       tenacity
                       INTEGER
                       DEFAULT
                       0,
                       flat_movement_speed
                       INTEGER
                       DEFAULT
                       0,
                       percent_movement_speed
                       INTEGER
                       DEFAULT
                       0,
                       on_hit_damage
                       INTEGER
                       DEFAULT
                       0
                   )
                   """)

    # 3. Commit changes and close the connection safely
    conn.commit()
    conn.close()
    print("Database and 'items' table created successfully!")


if __name__ == "__main__":
    init_database()