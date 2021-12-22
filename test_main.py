import sqlite3

conn = sqlite3.connect("db.db")
cursor = conn.cursor()

fix_conn = sqlite3.connect("fix_db.db")
fix_cursor = fix_conn.cursor()

# Check parts
def check_parts():
    weapon_title, hull_title, engine_title = [], [], []
    fix_weapon_title, fix_hull_title, fix_engine_title = [], [], []

    self_weapon, self_hull, self_engine = [], [], []

    ######## Weapon ########
    # Title
    cursor.execute("SELECT weapon FROM Ships")
    weapon_title = cursor.fetchall()

    fix_cursor.execute("SELECT weapon FROM Ships")
    fix_weapon_title = fix_cursor.fetchall()

    weapon, hull, engine = [], [], []
    fix_weapon, fix_hull, fix_engine = [], [], []

    # Weapon
    cursor.execute("SELECT * FROM Weapons")
    weapon = cursor.fetchall()

    fix_cursor.execute("SELECT * FROM Weapons")
    fix_weapon = fix_cursor.fetchall()

    ## Выбор нужного оружия
    # 0 - title  1 - reload_speed  2 - rotation_speed  3 - diameter  4 - power_volley
    # 5 - count
    for i in range(20):
        word = ''
        main_split, fix_split = [], []

        if weapon_title in weapon[i]:
            main_split = list(weapon[i])
            fix_split = list(fix_weapon[i])
            print(weapon[i])

            for k in range(1, 6):
                if main_split[k] != fix_split[k]:
                    if k == 1:
                        word = 'reload_speed'
                    elif k == 2:
                        word = 'rotation_speed'
                    elif k == 3:
                        word = 'diameter'
                    elif k == 4:
                        word = 'power_volley'
                    elif k == 5:
                        word = 'count'
                    print("{}: {}, was {}".format(word, main_split[k], fix_split[k]))
                    break


    ######## Hull ########
    # Title
    cursor.execute("SELECT hull FROM Hulls")
    hull_title = cursor.fetchall()

    fix_cursor.execute("SELECT hull FROM Hulls")
    fix_hull_title = fix_cursor.fetchall()

    # Hull
    cursor.execute("SELECT * FROM Hulls")
    hull = cursor.fetchall()

    fix_cursor.execute("SELECT * FROM Hulls")
    fix_hull = fix_cursor.fetchall()

    ## Выбор нужного корпуса
    # 0 - title  1 - armor  2 - type  3 - capacity
    for i in range(5):
        word = ''
        main_split, fix_split = [], []

        if hull_title in hull[i]:
            main_split = list(hull[i])
            fix_split = list(fix_hull[i])
            print(weapon[i])

            for k in range(1, 4):
                if main_split[k] != fix_split[k]:
                    if k == 1:
                        word = 'armor'
                    elif k == 2:
                        word = 'type'
                    elif k == 3:
                        word = 'capacity'
                    print("{}: {}, was {}".format(word, main_split[k], fix_split[k]))
                    break


    ######## Engine ########
    # Title
    cursor.execute("SELECT engine FROM Engine")
    engine_title = cursor.fetchall()

    fix_cursor.execute("SELECT engine FROM Engine")
    fix_engine_title = fix_cursor.fetchall()

    # Engine
    cursor.execute("SELECT * FROM Engine")
    engine = cursor.fetchall()

    fix_cursor.execute("SELECT * FROM Engine")
    fix_engine = fix_cursor.fetchall()

    ## Выбор нужного двигателя
    # 0 - title  1 - power  2 - type
    for i in range(6):
        word = ''
        main_split, fix_split = [], []

        if engine_title in engine[i]:
            main_split = list(weapon[i])
            fix_split = list(fix_weapon[i])
            print(weapon[i])

            for k in range(1, 3):
                if main_split[k] != fix_split[k]:
                    if k == 1:
                        word = 'power'
                    elif k == 2:
                        word = 'type'
                    print("{}: {}, was {}".format(word, main_split[k], fix_split[k]))
                    break


def test_ship():
    ship, fix_ship = [], []

    cursor.execute("SELECT ship FROM Ships")
    ship = cursor.fetchall()

    fix_cursor.execute("SELECT ship FROM Ships")
    fix_ship = fix_cursor.fetchall()
    check_parts()