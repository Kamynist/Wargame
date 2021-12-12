import sqlite3
import random

conn = sqlite3.connect("db.db")
cursor = conn.cursor()

fix_conn = sqlite3.connect("fix_db.db")
fix_cursor = fix_conn.cursor()

def initialization_main_db():
    request = tuple()

    # Weapon
    for i in range(20):
        request = "Weapon" + str(i), random.randint(1, 20), random.randint(1, 20),\
                  random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)
        cursor.execute("INSERT OR REPLACE INTO Weapons VALUES(?, ?, ?, ?, ?, ?)", request)
        conn.commit()
    # Hull
    for i in range(5):
        request = "Hull" + str(i), random.randint(1, 20), random.randint(1, 20), \
                  random.randint(1, 20)
        cursor.execute("INSERT OR REPLACE INTO Hulls VALUES(?, ?, ?, ?)", request)
        conn.commit()
    # Engine
    for i in range(6):
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

def initialization_fixture_db():
    request = tuple()


    # Weapons
    cursor.execute("SELECT reload_speed FROM Weapons")
    reload_speed = cursor.fetchall()

    cursor.execute("SELECT rotation_speed FROM Weapons")
    rotation_speed = cursor.fetchall()

    cursor.execute("SELECT diameter FROM Weapons")
    diameter = cursor.fetchall()

    cursor.execute("SELECT power_volley FROM Weapons")
    power_volley = cursor.fetchall()

    cursor.execute("SELECT count FROM Weapons")
    count = cursor.fetchall()

    for i in range(20):
        choice = random.randint(2, 6)
        if choice == 2:
            request = "Weapon" + str(i), random.randint(1, 20), rotation_speed[i], \
                      diameter[i], power_volley[i], count[i]
        elif choice == 3:
            request = "Weapon" + str(i), reload_speed[i], random.randint(1, 20), \
                      diameter[i], power_volley[i], count[i]
        elif choice == 4:
            request = "Weapon" + str(i), reload_speed[i], rotation_speed[i], \
                      random.randint(1, 20), power_volley[i], count[i]
        elif choice == 5:
            request = "Weapon" + str(i), reload_speed[i], rotation_speed[i], \
                      diameter[i], random.randint(1, 20), count[i]
        elif choice == 6:
            request = "Weapon" + str(i), reload_speed[i], rotation_speed[i], \
                      diameter[i], power_volley[i], random.randint(1, 20)

        fix_cursor.execute("INSERT OR REPLACE INTO Weapons VALUES(?, ?, ?, ?, ?, ?)",
                           request)


    # Hull
    cursor.execute("SELECT armor FROM Hulls")
    armor = cursor.fetchall()

    cursor.execute("SELECT type FROM Hulls")
    type = cursor.fetchall()

    cursor.execute("SELECT capacity FROM Hulls")
    capacity = cursor.fetchall()

    for i in range(5):
        choice = random.randint(2, 4)
        if choice == 2:
            request = "Hull" + str(i), random.randint(1, 20), type[i], capacity[i]
        elif choice == 3:
            request = "Hull" + str(i), armor, random.randint(1, 20), capacity[i]
        elif choice == 4:
            request = "Hull" + str(i), armor, type[i], random.randint(1, 20)

        fix_cursor.execute("INSERT OR REPLACE INTO Hulls VALUES(?, ?, ?, ?)",
                           request)


    # Engine
    cursor.execute("SELECT power FROM Engine")
    power = cursor.fetchall()

    cursor.execute("SELECT type = FROM Engine")
    type = cursor.fetchall()

    for i in range(6):
        choice = random.randint(2, 3)
        if choice == 2:
            request = "Engine" + str(i), random.randint(1, 20), type[i]
        elif choice == 3:
            request = "Engine" + str(i), power[i], random.randint(1, 20)

        fix_cursor.execute("INSERT OR REPLACE INTO Engine VALUES(?, ?, ?)",
                           request)


    # Ships
    cursor.execute("SELECT weapon = FROM Ships")
    weapon = cursor.fetchall()

    cursor.execute("SELECT hull FROM Ships")
    hull = cursor.fetchall()

    cursor.execute("SELECT engine = FROM Ships")
    engine = cursor.fetchall()

    for i in range(200):
        choice = random.randint(2, 4)

        if choice == 2:
            request = "Ship" + str(i), weapon[random.randint(0, 20)], hull[i], engine[i]
        elif choice == 3:
            request = "Ship" + str(i), weapon[i], hull[random.randint(0, 4)], engine[i]
        elif choice == 4:
            request = "Ship" + str(i), weapon[i], hull[i], engine[random.randint(0, 5)]

        fix_cursor.execute("INSERT OR REPLACE INTO Ships VALUES(?, ?, ?, ?)",
                           request)