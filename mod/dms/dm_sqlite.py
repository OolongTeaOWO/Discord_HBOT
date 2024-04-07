import sqlite3


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()

def create_table():
    with DatabaseConnection("member.db") as cursor:
        cursor.execute('''CREATE TABLE IF NOT EXISTS members (
                            member_id INTEGER PRIMARY KEY,
                            added_members TEXT
                        )''')

def get_added_members(member_id):
    with DatabaseConnection("member.db") as cursor:
        cursor.execute('''SELECT added_members FROM members WHERE member_id=?''', (member_id,))
        result = cursor.fetchone()
        return result[0] if result else None

def update_added_members(member_id, new_added_members):
    with DatabaseConnection("member.db") as cursor:
        cursor.execute('''UPDATE members SET added_members=? WHERE member_id=?''', (new_added_members, member_id))
