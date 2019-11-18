import sqlite3
import webbrowser
import base64


#asks the user for a record number between 1 and 24(Now 29), other values must be ignored and the user prompted again. Character q quits the program.

enterKey = input("Enter a number between 1 and 29: ")
try:   
    if int(enterKey) in range(1,30):
        print(int(enterKey))
    if int(enterKey) not in range (1,30):
        while int(enterKey) not in range(1,30):
            enterKey = input("Enter a number between 1 and 29: ")
            if enterKey == 'q':
                exit()
            if enterKey != 'q': 
                enterKey = int(enterKey)
        if int(enterKey) in range(1,30):
            print(enterKey)

except:
    if enterKey == 'q':
        exit()


#writes and executes a SQLite3 query to extract the Link field associated with the record
con = sqlite3.connect('week10.db')
cur = con.cursor()
run = cur.execute( "select link from Lab10 where id = ?", (enterKey,))
place = cur.fetchone()
for each in place:
    #decodes the base64 encoded value of the URL
    decodedValue=(base64.b64decode(each))
#opens a web browser with the decoded URL
webbrowser.open(decodedValue)

#for that specific record, asks the user for name of the city  and the country and student
cityName = input("What is the name of the city?: ")
countryName = input("What is the name of the country?: ")
studentName = input("What is the name of the student who came from this location?: ")

#and updates the record
cur.execute("update Lab10 set City = ? where id = ?", (cityName, enterKey,))
cur.execute("update Lab10 set Country = ? where id = ?", (countryName, enterKey,))
cur.execute("update Lab10 set  Student = ? where id = ?", (studentName, enterKey,))
#saves changes
con.commit()
print("The database table has been updated at the row where ID is " + enterKey)
con.close()