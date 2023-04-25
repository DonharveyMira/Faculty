#inventory database
import sqlite3


class Meds_Database:
    def __init__(self, meds_db):
        self.con = sqlite3.connect(meds_db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS inventory(
            id Integer Primary Key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, age, doj, email, gender, contact, address):
        self.cur.execute("insert into inventory values (NULL,?,?,?,?,?,?,?)",
                         (name, age, doj, email, gender, contact, address))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from inventory")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from inventory where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, age, doj, email, gender, contact, address):
        self.cur.execute(
            "update inventory set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?",
            (name, age, doj, email, gender, contact, address, id))
        self.con.commit()
