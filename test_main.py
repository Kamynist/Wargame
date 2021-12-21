import sqlite3

conn = sqlite3.connect("db.db")
cursor = conn.cursor()

fix_conn = sqlite3.connect("fix_db.db")
fix_cursor = fix_conn.cursor()


def test_weapons():
    ship, fix_ship, weapon, fix_weapon = [], [], [], []
    fail_test = False

    cursor.execute("SELECT ship FROM Ships")
    fix_cursor.execute("SELECT ship FROM Ships")

    ship = cursor.fetchall()
    fix_ship = fix_cursor.fetchall()

    cursor.execute("SELECT weapon FROM Ships")
    fix_cursor.execute("SELECT weapon FROM Ships")

    weapon = cursor.fetchall()
    fix_weapon = fix_cursor.fetchall()

    assert ship == fix_ship
    assert weapon == fix_weapon