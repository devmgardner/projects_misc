def build():
    import sqlite3 as sq,os,sys
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)
    dbcon = sq.connect(os.path.join(currentdir,'Time.db'))
    dbcur = dbcon.cursor()
    with open(os.path.join(currentdir,'build.sql'),'r') as shand:
        script = shand.read()
        dbcur.executescript(script)
    dbcon.commit()
    dbcon.close()
build()