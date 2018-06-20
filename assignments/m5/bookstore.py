import sqlite3
Mybooks=sqlite3.connect('booksdb.db')
curbooks=Mybooks.cursor()

def showbook(ttl):
    sql="SELECT * FROM bookstb WHERE TITLE='"+str(ttl)+"';"
    curbooks.execute(sql)
    record=curbooks.fetchone()
    if record==None:
        return 0
    print (record)
    pri=record[2]
    return pri

totcost=0.0
yorn='y'
while yorn=='y':
    ttl=input('Book Title:')
    cost=showbook(ttl)
    if cost==0:
        print("No such book present")
        yorn=input('Add more books?y/n:')
    else:
        no=float(input('Number of Copies:'))
        totcost=totcost+no*cost
        yorn=input('Add more books?y/n:')
        if yorn=='n':
            print ('Total Cost:',totcost)
