import MySQLdb as mdb
import sys

class Bookstore:

    #constructor
    def __init__(self):
        self.con = None
        self.cur = None

    #authenticate bookstore credentials
    def autheticate(self,bid,passw):
        if uid == 'bookstore' and passw == 'bk456':
            return True
        else:
            return False    

    #retreive textbook selection for a given course
    def retrieve(self,cid,sem,y):
        self.connection()
        d = y+'-'
        d = d+self.semtomonth(sem)
        self.cur.execute("SELECT * FROM book,uses WHERE book.isbn=uses.isbn AND courseid = %s AND fromdate<DATE(%s) and usedtill>DATE(%s)",(cid,d,d))
        rows = self.cur.fetchall()
        if not rows:
            print("No Records")
        else:
            print(" ")
            c=1
            for row in rows:
                c_str = str(c)
                print c_str + ": " + row[1]
                c+=1

        self.closeconnection()

    #retrieve all textbook selections for a given semester
    def retrieveall(self,sem,y):
        self.connection()
        d = y+'-'
        d = d+self.semtomonth(sem)
        self.cur.execute("SELECT * FROM book,uses WHERE book.isbn=uses.isbn AND fromdate<DATE(%s) and usedtill>DATE(%s)",(d,d))
        rows = self.cur.fetchall()
        if not rows:
            print("No Records")
        else:
            print(" ")
            c=1
            for row in rows:
                c_str = str(c)
                print c_str + ": " + row[1]
                c+=1

        self.closeconnection()

    #connect to database
    def connection(self):
        
        conn = None

        try :
            conn = mdb.connect("127.0.0.1", "root",
                "", "textbook")
            
        except mdb.Error, e:
          
            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        self.con = conn 
        self.cur = self.con.cursor()

    #close connection to database
    def closeconnection(self):
        self.con.close()
        self.cur.close()
        
    #convert semester to formatted string
    def semtomonth(self,s):
        m = '01'
        if s == 'spring':
            m='01'
        elif s == 'summer':
            m='05'
        elif s == 'fall':
            m='07'
        mmdd = m+'-02'
        return mmdd


