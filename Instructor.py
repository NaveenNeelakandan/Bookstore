import MySQLdb as mdb
import sys

class Instructor:

    #constructor
    def __init__(self):
        self.con = None
        self.cur = None

    #function to authenticate instructor credentials
    def authenticate(self,bid,passw):
        self.connection()
        self.cur.execute("SELECT * FROM professor WHERE id = %s AND password = %s",(bid,passw))
        rows = self.cur.fetchall()
        self.closeconnection()
        if not rows:
            return False
        else:
            return True
        
    #inserting a book into the database 
    def insert(self,cid,y,sem,isb,titl,on_sup,pr_us,ed,fr_cpy,pri,uid):
        self.connection()
        sem = self.semtomonth2(sem)
        yr = str(y)
        frmd= yr+"-"+sem
        y=y+3
        yr = str(y)
        tod=yr+"-"+sem
        
        #insert into book table
        try:
            self.cur.execute("INSERT INTO book(isbn,title,online_support,previous_use,edition,free_copy,price) VALUES(%s,%s,%s,%s,%s,%s,%s)",(isb,titl,on_sup,pr_us,ed,fr_cpy,pri))
        except:
            print("Unable to Insert -- Check if book already exists")
            self.closeconnection()
            return

        self.cur.execute("SELECT ssn FROM professor WHERE id=%s",(uid))
        sn = self.cur.fetchone()
        sn=sn[0]

        #insert into recommendation table
        self.cur.execute("INSERT INTO recommendation(ssn,isbn) VALUES(%s,%s)",(sn,isb))

        #insert into uses table
        self.cur.execute("INSERT INTO uses(courseid,isbn,fromdate,todate,usedtill) VALUES(%s,%s,%s,%s,%s)",(cid,isb,frmd,tod,tod))

        self.con.commit()
        print("Sucessfully Added Textbook")
        self.closeconnection()

    #removing a textbook from a course
    def remove(self,cid,sem,y):
        self.connection()
        r = self.retrieve(cid,sem,y)
        if not r:
            print("No records found")
        else:
            book_choice = raw_input("Select book ")
        try:
            book_choice = int(book_choice)
            book_choice = book_choice-1
            b = r[book_choice]
            self.cur.execute("SELECT * FROM book,uses WHERE book.isbn=uses.isbn AND book.isbn=%s AND todate>DATE(%s)",(b[0],'2012-01-01'))
            rows = self.cur.fetchall()
            if not rows:
                self.cur.execute("UPDATE uses SET usedtill=DATE(%s) WHERE isbn=%s AND courseid=%s",('2012-01-01',b[0],cid))
            else:
                confirm = raw_input("This will violate the 3-year rule. Continue? Y/N")
                confirm = confirm.lower()
                if confirm == 'y':
                    self.cur.execute("UPDATE uses SET usedtill=DATE(%s) WHERE isbn=%s AND courseid=%s",('2012-01-01',b[0],cid))    
              
        except: 
            print("invalid choice")
        self.con.commit()
        print("Sucessfully Removed Textbook")
        self.closeconnection()

    #retrieving a textbook for a course
    def retrieve(self,cid,sem,y):
        self.connection()
        y = str(y)
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

        return rows
        self.closeconnection()

    #check if instructor teaches course
    def coursescheck(self,uid,cid):
        self.connection()
        self.cur.execute("SELECT ssn FROM professor WHERE id=%s",(uid))
        sn = self.cur.fetchone()
        sn=sn[0]
        self.cur.execute("SELECT * FROM teaches WHERE courseid=%s AND ssn=%s",(cid,sn))
        rows = self.cur.fetchall()
        self.closeconnection()
        if not rows:
            print("Invalid Course Selection - Not instructor for course")
            return False
        else:
            return True
        
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

    def semtomonth2(self,s):
        m = '01'
        if s == 'spring':
            m='01'
        elif s == 'summer':
            m='05'
        elif s == 'fall':
            m='07'
        mmdd = m+'-01'
        return mmdd
 


