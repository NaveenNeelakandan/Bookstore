from Registrar import *
from Bookstore import *
from Instructor import *

def main():

    print("University Textbook Database")
    print(" ")

    #get user type
    print("Enter User Type")
    print("1: Instructor")
    print("2: Registrar")
    print("3: Bookstore")

    user = raw_input("Enter: ")
    while user != '1' and user != '2' and user != '3':
        print("Invalid choice")
        user = raw_input("Enter: ")

    print(" ")

    #get user authentication information
    userid = raw_input("Input Id: ")
    password = raw_input("Enter Password: ")

    #if user is a instructor
    if user == '1':
        i = Instructor()
##        while(i.authenticate(userid,password) == False):
##
##            print("Authentication Failure")
##            userid = raw_input("Input Id: ")
##            password = raw_input("Enter Password: ")

        
        loop = True
        while (loop == True):
            print(" ")

            #show operations
            print("Select operation")
            print("1: Add new textbook")
            print("2: Remove textbook")
            print("3: View textbook Selection for course")
            choice = raw_input("Enter: ")
            print("")

            #adding new textbook
            if choice == '1':

                #validate if instructor teaches course
                teaches = False
                while (teaches == False):
                    cid = raw_input("Enter course id: ")
                    cid = cid.lower()
                    teaches = i.coursescheck(userid,cid)

                #validate year input
                flag = False
                while flag == False:
                    year = raw_input("Enter Year: ")
                    if(year.isdigit() and len(year)==4):
                        year = int(year)
                        if(year >= 2012):
                            flag = True
                        else:
                            print("Cannot Change Past Records!")
                    else:
                        print("Enter valid year")

                #validate semester input
                flag = False
                while flag == False:
                    semester = raw_input("Enter Semester: ")
                    semester = semester.lower()
                    if semester == 'fall':
                        flag = True
                    elif semester == 'summer':
                        flag = True
                    elif semester == 'spring':
                        flag = True
                    else:
                        print("Enter valid semester ")
                        flag = False

                #validate isbn input
                flag = False
                while flag == False:        
                    isbn = raw_input("Enter ISBN: ")
                    if len(isbn)!=13 or isbn.isdigit()==False:
                        print("Enter valid ISBN")
                        flag = False
                    else:
                        isbn = int(isbn)
                        flag = True

                #validate title input
                flag = False
                while flag == False:        
                    title = raw_input("Enter Title: ")
                    if len(title) > 20:
                        print("Enter shorter title")
                        flag = False
                    else:
                        flag = True

                #validate online_support input
                flag = False
                while flag == False:        
                    online_support = raw_input("Online Support? Y/N ")
                    online_support = online_support.lower()
                    if online_support!= 'n' and online_support!='y':
                        print("Enter y/n only!")
                        flag = False
                    else:
                        if online_support == 'y':
                            online_support = 1
                        else:
                            online_support = 0
                        flag = True      

                #validate previous_use input
                flag = False
                while flag == False:        
                    previous_use = raw_input("Previous Use? Y/N ")
                    previous_use = previous_use.lower()
                    if previous_use!= 'n' and previous_use!='y':
                        print("Enter y/n only!")
                        flag = False
                    else:
                        if previous_use == 'y':
                            previous_use = 1
                        else:
                            previous_use = 0
                        flag = True   

                #validate edition input        
                flag = False
                while flag == False:        
                    edition = raw_input("Enter Edition: ")
                    if edition.isdigit()==False:
                        print("Enter digits only")
                        flag = False
                    else:
                        edition = int(edition)
                        flag = True        

                #validate free_copy input        
                flag = False
                while flag == False:        
                    free_copy = raw_input("Free Copy? Y/N ")
                    free_copy = free_copy.lower()
                    if free_copy!= 'n' and free_copy!='y':
                        print("Enter y/n only!")
                        flag = False
                    else:
                        if free_copy == 'y':
                            free_copy = 1
                        else:
                            free_copy = 0
                        flag = True

                #validate price input
                flag = False
                while flag == False:
                    try:
                        price = raw_input("Enter a price: ")
                        price = float(price)
                        flag = True
                    except ValueError:
                        print("You must enter a number")

                i.insert(cid,year,semester,isbn,title,online_support,previous_use,edition,free_copy,price,userid)

            #removing textbook                 
            elif choice == '2':

                #validate if instructor teaches course
                teaches = False
                while (teaches == False):
                    cid = raw_input("Enter course id: ")
                    cid = cid.lower()
                    teaches = i.coursescheck(userid,cid)

                #validate year input
                flag = False
                while flag == False:
                    year = raw_input("Enter Year: ")
                    if(year.isdigit()):
                        year = int(year)
                        if(year >= 2012):
                            flag = True
                        else:
                            print("Cannot Change Past Records!")
                    else:
                        print("Enter valid year")

                #validate semester input
                flag = False
                while flag == False:
                    semester = raw_input("Enter Semester: ")
                    semester = semester.lower()
                    if semester == 'fall':
                        flag = True
                    elif semester == 'summer':
                        flag = True
                    elif semester == 'spring':
                        flag = True
                    else:
                        print("Enter valid semester")
                        flag = False
                        
                i.remove(cid,semester,year)

            #view textbook selections
            elif choice == '3':

                #validate if instructor teaches course
                teaches = False
                while (teaches == False):
                    cid = raw_input("Enter course id: ")
                    teaches = i.coursescheck(userid,cid)

                #validate semester input
                flag = False
                while flag == False:
                    semester = raw_input("Enter Semester: ")
                    semester = semester.lower()
                    if semester == 'fall':
                        flag = True
                    elif semester == 'summer':
                        flag = True
                    elif semester == 'spring':
                        flag = True
                    else:
                        print("Enter valid semester")
                        flag = False

                #validate year input
                flag = False
                while flag == False:
                    year = raw_input("Enter year: ")
                    if year.isdigit() and len(year)==4:
                        flag = True
                    else:
                         print("Enter Valid year")        
                
                i.retrieve(cid,semester,year)

            else:
                print("Invalid choice")

            #ask if user wants to continue
            print("")
            u = raw_input("Continue?Y/N ")
            u=u.lower()
            if u == 'n' or u == 'N':
                loop = False

    #if user is registrar
    if user == '2':

        r = Registrar()

##        while(r.authenticate(userid,password) == False):
##
##            print("Authentication Failure")
##            userid = raw_input("Input Id: ")
##            password = raw_input("Enter Password: ")
        loop = True
        print(" ")

        while(loop == True):

            #show operations
            print("Select operation")
            print("1: View Violations")
            print("2: View textbook Selection for course")
            choice = raw_input("Enter: ")
            print("")

            #view violations
            if choice == '1':
                print("Select Time period to view violations")

                #validate semester input
                flag = False
                while flag == False:
                    semester = raw_input("Enter Semester: ")
                    semester = semester.lower()
                    if semester == 'fall':
                        flag = True
                    elif semester == 'summer':
                        flag = True
                    elif semester == 'spring':
                        flag = True
                    else:
                        print("Enter valid semester")
                        flag = False

                #validate year input
                flag = False
                while flag == False:
                    year = raw_input("Enter year: ")
                    if year.isdigit() and len(year)==4:
                        flag = True
                    else:
                         print("Enter Valid year")

                r.violation(semester,year)
                
            #view textbook selection
            elif choice == '2':
            
                cid = raw_input("Enter course id: ")
                cid = cid.lower()

                #validate semester input
                flag = False
                while flag == False:
                    semester = raw_input("Enter Semester: ")
                    semester = semester.lower()
                    if semester == 'fall':
                        flag = True
                    elif semester == 'summer':
                        flag = True
                    elif semester == 'spring':
                        flag = True
                    else:
                        print("Enter valid semester")
                        flag = False

                #validate year input
                flag = False
                while flag == False:
                    year = raw_input("Enter year: ")
                    if year.isdigit() and len(year)==4:
                        flag = True
                    else:
                         print("Enter Valid year")

                r.retrieve(cid,semester,year)
                

            else:
                print("Invalid choice")

            #ask if user wants to continue
            print("")
            u = raw_input("Continue?Y/N ")
            u=u.lower()
            if u == 'n' or u == 'N':
                loop = False
                
    #if user is bookstore  
    if user == '3':
        print()
        b = Bookstore()
##      while(b.authenticate(userid,password) == False):
##
##            print("Authentication Failure")
##            userid = raw_input("Input Id: ")
##            password = raw_input("Enter Password: ")

        loop = True
        print(" ")

        while(loop == True):

            #show operations 
            print("Select operation")
            print("1: View all textbook Selections")
            print("2: View textbook Selection for course")
            choice = raw_input("Enter: ")
            print("")

            #view all textbook selections
            if choice == '1':

                #validate semester input
                flag = False
                while flag == False:
                    semester = raw_input("Enter Semester: ")
                    semester = semester.lower()
                    if semester == 'fall':
                        flag = True
                    elif semester == 'summer':
                        flag = True
                    elif semester == 'spring':
                        flag = True
                    else:
                        print("Enter valid semester")
                        flag = False

                #validate year input
                flag = False
                while flag == False:
                    year = raw_input("Enter year: ")
                    if year.isdigit() and len(year)==4:
                        flag = True    
                    else:
                        print("Enter valid year")
                
                b.retrieveall(semester,year)

            elif choice == '2':

                cid = raw_input("Enter course id: ")
                cid = cid.lower()

                #validate semester input                
                flag = False
                while flag == False:
                    semester = raw_input("Enter Semester: ")
                    semester = semester.lower()
                    if semester == 'fall':
                        flag = True
                    elif semester == 'summer':
                        flag = True
                    elif semester == 'spring':
                        flag = True
                    else:
                        print("Enter valid semester")
                        flag = False

                #validate year input
                flag = False
                while flag == False:
                    year = raw_input("Enter year: ")
                    if year.isdigit() and len(year)==4:
                        flag = True    
                    else:
                        print("Enter valid year")
                b.retrieve(cid,semester,year)

            else:
                print("Invalid choice")

            #ask if user wants to continue    
            print("")
            u = raw_input("Continue?Y/N ")
            u=u.lower()
            if u == 'n' or u == 'N':
                loop = False

if __name__ == "__main__":
    main()
