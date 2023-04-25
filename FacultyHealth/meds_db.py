#meds database
import sqlite3


class Meds_Database:
    def __init__(self, meds_db):
        self.con = sqlite3.connect(meds_db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS inventory(
            id Integer Primary Key,
            code,
            description,
            onHand,
            max
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, code, description, onHand, max):
        self.cur.execute("insert into meds values (NULL,?,?,?,?)",
                         (code, description, onHand, max))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from meds")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from meds where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, code, description, onHand, max):
        self.cur.execute(
            "update meds set code=?, description=?, onHand=?, max=?, where id=?",
            (code, description, onHand, max, id))
        self.con.commit()
