import sqlite3
def create_db():
    con=sqlite3.connect(database="GradeMaster.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charges text, description text)")
    conn.commit()