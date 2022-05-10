import mysql.connector

def quick():
    import random
#variables
    score=0
    rand=0
    update=[]
#asking the users name
    name=str(input("Enter name:"))
#main program
    for i in range(5):
        n1=random.randint(0,11)#importing 2 random values
        n2=random.randint(0,11)
#putting the whole question in a single line
        question=int(input(str(n1)+"+"+str(n2)+"="))
#getting the real answer to see if it matches with the question
        ans=n1+n2
#checking if the answers match the useres input
        if question == ans:
            #keeping track of the score
            score = score +1
            update.append(str(n1)+' + '+str(n2)+' = '+str(question)+'(Answer is '+str(ans)+')[Correct]')
        else:
            update.append(str(n1)+' + '+str(n2)+' = '+str(question)+'(Answer is '+str(ans)+')[Incorrect]')

    for val in range(5):
        print(update[val])

        
    
#printing the results    
    print("   Results")
    print("Your name is: ",name)
    print("you have got",score,"/5 correct")
    print("your scored : ",(score/5)*100,"/100")

#Saving the data to a database
    import mysql.connector
    #open the connection with dictonary
    conDict={"host":"localhost",
             "database":"project",
             "user":"root",
             "password":""}
    
    db=mysql.connector.connect(**conDict)
    
#prepare a cursor object using cursor() methord
    cursor=db.cursor()
    
#execute sql query usinng execute() methord
    sqltxt="INSERT INTO quickgameresults (name,correct,totalquestions,percentage) VALUES (%s,%s,%s,%s)"
    userstxt=(name,score,"5",(score/5)*100)
    cursor.execute(sqltxt,userstxt)
#inserting the change
    db.commit()
    
#closing the connection    
    db.close()
    
