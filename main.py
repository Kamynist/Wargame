import sqlite3
from script import initialization_main_db, initialization_fixture_db

conn = sqlite3.connect("db.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

fix_conn = sqlite3.connect("fix_db.db")
fix_cursor = fix_conn.cursor()


def create_base_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Ships(
                        ship TEXT PRIMARY KEY,
                        weapon TEXT,
                        hull TEXT,
                        engine TEXT,
                        FOREIGN KEY (weapon) REFERENCES Weapons(weapon),
                        FOREIGN KEY (hull) REFERENCES Hulls(hull),
                        FOREIGN KEY (engine) REFERENCES Engine(engine));
                    """)

    conn.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Weapons(
                        weapon TEXT PRIMARY KEY,
                        reload_speed INT,
                        rotation_speed INT,
                        diameter INT,
                        power_volley INT,
                        count INT);
                    """)
    conn.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Hulls(
                        hull TEXT PRIMARY KEY,
                        armor INT,               
                        type INT,
                        capacity INT);
                    """)
    conn.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Engine(
                        engine TEXT PRIMARY KEY,
                        power INT,
                        type INT);
                    """)
    conn.commit()

def create_fixture_db():
    fix_cursor.execute("""CREATE TABLE IF NOT EXISTS Ships(
                            ship TEXT PRIMARY KEY,
                            weapon TEXT,
                            hull TEXT,
                            engine TEXT,
                            FOREIGN KEY (weapon) REFERENCES Weapons(weapon),
                            FOREIGN KEY (hull) REFERENCES Hulls(hull),
                            FOREIGN KEY (engine) REFERENCES Engine(engine));
                        """)

    fix_conn.commit()

    fix_cursor.execute("""CREATE TABLE IF NOT EXISTS Weapons(
                            weapon TEXT PRIMARY KEY,
                            reload_speed INT,
                            rotation_speed INT,
                            diameter INT,
                            power_volley INT,
                            count INT);
                        """)
    fix_conn.commit()

    fix_cursor.execute("""CREATE TABLE IF NOT EXISTS Hulls(
                            hull TEXT PRIMARY KEY,
                            armor INT,
                            type INT,
                            capacity INT);
                        """)
    fix_conn.commit()

    fix_cursor.execute("""CREATE TABLE IF NOT EXISTS Engine(
                            engine TEXT PRIMARY KEY,
                            power INT,
                            type INT);
                        """)
    fix_conn.commit()

create_base_db()
create_fixture_db()
initialization_main_db()
initialization_fixture_db()

conn.close()
fix_conn.close()