import _sqlite3

try:
    db = _sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    fh = open('world.sql', 'r')
    script = fh.read()
    cursor.executescript(script)
    print("Data Imported Successfully")
except Exception as e:
    db.rollback()
    raise e
finally:
    db.close()
