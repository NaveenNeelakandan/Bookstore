import MySQLdb as mdb
import sys

class Registrar:

    #constructor
    def __init__(self):
        self.con = None
        self.cur = None        

    #authenticate registrar credentials
    def authenticate(self,uid,passw):
        if uid == 'registrar' and passw == 'r357':
            return True
        else:
            return False
        
    #retrieving a textbook for a course    
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

    #retreiving all textbooks that violate the 3-year rule   
    def violation(self,sem,y):
        self.connection()
        d = y+'-'
        d = d+self.semtomonth(sem)
        self.cur.execute("SELECT * FROM book,uses WHERE book.isbn=uses.isbn AND todate>DATE(%s) AND usedtill<DATE(%s)",(d,d))
        rows = self.cur.fetchall()
        if not rows:
            print("No violations")
        else:
            print(" ")
            for row in rows:
                print row[7] + "--" + row[1]

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
        #print("Connection Established")

    #close connection to database 
    def closeconnection(self):
        self.con.close()
        self.cur.close()
        #print("Connection closed")

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

    
