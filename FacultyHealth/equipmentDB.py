#equipment database
import sqlite3


class Equipment_Database:
    def __init__(self, equipment_db):
        self.con = sqlite3.connect(equipment_db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS equipment(
            id Integer Primary Key,
            equipment text,
            quantity text

        )
        """

        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, equipment, quantity):
        self.cur.execute("insert into equipment values (NULL,?,? )",
                         (equipment, quantity))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from equipment")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from equipment where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, equipment, quantity):
        self.cur.execute(
            "update equipment, quantity where id=?",
            (equipment, quantity, id))
        self.con.commit()
