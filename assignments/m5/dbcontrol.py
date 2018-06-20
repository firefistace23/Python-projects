import sqlite3
MyBooks=sqlite3.connect('booksdb.db')
curbooks=MyBooks.cursor()
##curbooks.execute('''CREATE TABLE bookstb (
##    TITLE  STRING PRIMARY KEY,
##    AUTHOR STRING,
##    PRICE  REAL
##);''')

def addbook(ttl='Harry Potter',auth='J.K. Rowling',pri=250):
    curbooks.execute('''INSERT INTO bookstb (TITLE,AUTHOR,PRICE) VALUES(?,?,?);''',(ttl,auth,pri))
    MyBooks.commit()

def showbook(ttl):
    sql="SELECT * FROM bookstb WHERE TITLE='"+str(ttl)+"';"
    curbooks.execute(sql)
    while True:
        record=curbooks.fetchone()
        if record==None:
            break
        print (record)



    
