import sqlite3
import random

conn = sqlite3.connect("db.db")
cursor = conn.cursor()

fix_conn = sqlite3.connect("fix_db.db")
fix_cursor = fix_conn.cursor()

def initialization_main_db():
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

    weapon, hull, engine = [], [], []

    cursor.execute("SELECT weapon FROM Weapons")
    weapon = cursor.fetchall()

    cursor.execute("SELECT hull FROM Hulls")
    hull = cursor.fetchall()

    cursor.execute("SELECT engine FROM Engine")
    engine = cursor.fetchall()

    # Ships
    for i in range(200):

        request = 'Ships' + str(i), 'Weapon' + str(random.randint(0, 19)), \
                  'Hull' + str(random.randint(0, 19)), 'Engine' + str(random.randint(0, 19))

        cursor.execute("INSERT OR REPLACE INTO Ships VALUES(?, ?, ?, ?)", request)
        conn.commit()


def initialization_fixture_db():
    ######## Weapons ########
    weapon, reload_speed, rotation_speed, \
    diameter, power_volley, count = [], [], [], [], [], []

    cursor.execute("SELECT weapon FROM Weapons")
    weapon = cursor.fetchall()

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
            request = weapon[i] + reload_speed[random.randint(0, 20)] + rotation_speed[i] + \
                      diameter[i] + power_volley[i] + count[i]
        elif choice == 3:
            request = weapon[i] + reload_speed[i] + rotation_speed[random.randint(0, 19)] + \
                      diameter[i] + power_volley[i] + count[i]
        elif choice == 4:
            request = weapon[i] + reload_speed[i] + rotation_speed[i] + \
                      diameter[random.randint(0, 19)] + power_volley[i] + count[i]
        elif choice == 5:
            request = weapon[i] + reload_speed[i] + rotation_speed[i] + \
                      diameter[i] + power_volley[random.randint(0, 19)] + count[i]
        elif choice == 6:
            request = weapon[i] + reload_speed[i] + rotation_speed[i] + \
                      diameter[i] + power_volley[i] + count[random.randint(0, 19)]

        fix_cursor.execute("INSERT OR REPLACE INTO Weapons VALUES(?, ?, ?, ?, ?, ?)",
                           request)
        fix_conn.commit()



    # Hull
    hull, armor, type, capacity = [], [], [], []

    cursor.execute("SELECT hull FROM Hulls")
    hull = cursor.fetchall()

    cursor.execute("SELECT armor FROM Hulls")
    armor = cursor.fetchall()

    cursor.execute("SELECT type FROM Hulls")
    type = cursor.fetchall()

    cursor.execute("SELECT capacity FROM Hulls")
    capacity = cursor.fetchall()

    for i in range(5):
        choice = random.randint(2, 4)
        if choice == 2:
            request = hull[i] + armor[random.randint(0, 4)] + type[i] + capacity[i]
        elif choice == 3:
            request = hull[i] + armor[i] + type[random.randint(0, 4)] + capacity[i]
        elif choice == 4:
            request = hull[i] + armor[i] + type[i] + capacity[random.randint(0, 4)]

        fix_cursor.execute("INSERT OR REPLACE INTO Hulls VALUES(?, ?, ?, ?)",
                           request)
        fix_conn.commit()


    # Engine
    engine, power, type = [], [], []

    cursor.execute("SELECT engine FROM Engine")
    engine = cursor.fetchall()

    cursor.execute("SELECT power FROM Engine")
    power = cursor.fetchall()

    cursor.execute("SELECT type FROM Engine")
    type = cursor.fetchall()

    for i in range(6):
        choice = random.randint(2, 3)
        if choice == 2:
            request = engine[i] + power[random.randint(0, 5)] + type[i]
        elif choice == 3:
            request = engine[i] + power[i] + type[random.randint(0, 5)]

        fix_cursor.execute("INSERT OR REPLACE INTO Engine VALUES(?, ?, ?)",
                           request)
        fix_conn.commit()


    # Ships
    ship, weapon, hull, engine = [], [], [], []

    cursor.execute("SELECT ship FROM Ships")
    ship = cursor.fetchall()

    cursor.execute("SELECT weapon FROM Ships")
    weapon = cursor.fetchall()

    cursor.execute("SELECT hull FROM Ships")
    hull = cursor.fetchall()

    cursor.execute("SELECT engine FROM Ships")
    engine = cursor.fetchall()

    for i in range(200):
        choice = random.randint(2, 4)

        if choice == 2:
            request = ship[i] + weapon[random.randint(0, 20)] + hull[i] + engine[i]
        elif choice == 3:
            request = ship[i] + weapon[i] + hull[random.randint(0, 4)] + engine[i]
        elif choice == 4:
            request = ship[i] + weapon[i] + hull[i] + engine[random.randint(0, 5)]

        fix_cursor.execute("INSERT OR REPLACE INTO Ships VALUES(?, ?, ?, ?)",
                           request)
        fix_conn.commit()