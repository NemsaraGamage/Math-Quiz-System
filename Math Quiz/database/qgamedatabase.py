import mysql.connector

#open the connection with dictonary
conDict={"host":"localhost",
         "database":"project",
         "user":"root",
         "password":""}
    
db=mysql.connector.connect(**conDict)
    
#prepare a cursor object using cursor() mthord
cursor=db.cursor()
    
#execute sql query usinng execute() methord
cursor.execute("SELECT * FROM quickgameresults")

    
#fetch results using fetcall() methord
data=cursor.fetchall()

#printing the variavles
print()
print("Name","Correct","Questions","Percentage")
for item in data:
    print("\r")
    for a in item:
        print(a,end="\t")

#closing the connection
db.close()
