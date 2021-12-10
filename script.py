import sqlite3
import random

conn = sqlite3.connect("db.db")
cursor = conn.cursor()

fix_conn = sqlite3.connect("fix_db.db")
fix_cursor = fix_conn.cursor()


def initialization():
    # Weapon
    for i in range(20):
        request = tuple()
        request = "Weapon" + str(i), random.randint(1, 20), random.randint(1, 20),\
                  random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)
        cursor.execute("INSERT OR REPLACE INTO Weapons VALUES(?, ?, ?, ?, ?, ?)", request)
        conn.commit()
    # Hull
    for i in range(5):
        request = tuple()
        request = "Hull" + str(i), random.randint(1, 20), random.randint(1, 20), \
                  random.randint(1, 20)
        cursor.execute("INSERT OR REPLACE INTO Hulls VALUES(?, ?, ?, ?)", request)
        conn.commit()
    # Engine
    for i in range(6):
        request = tuple()
        request = "Engine" + str(i), random.randint(1, 20), random.randint(1, 20)
        cursor.execute("INSERT OR REPLACE INTO Engine VALUES(?, ?, ?)", request)
        conn.commit()

    # Ships
    for i in range(200):
        cursor.execute("SELECT weapon FROM Weapons")
        weapon = cursor.fetchall()

        cursor.execute("SELECT hull FROM Hulls")
        hull = cursor.fetchall()

        cursor.execute("SELECT engine FROM Engine")
        engine = cursor.fetchall()

        request = "Ships " + str(i), weapon[random.randint(0, 20)],\
                  hull[random.randint(0, 4)], engine[random.randint(0, 5)]
        cursor.execute("INSERT OR REPLACE INTO Ships VALUES(?, ?, ?, ?)", request)
        conn.commit()
