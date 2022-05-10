def ez():
    import random
    #variables
    score=0
    rand=0
    update=[]
    name=str(input("Enter name: "))
    times=int(input("How many questions would you like? = "))
    print()
    #main program
    for i in range(times):
        n1=random.randint(0,11)#importing 2 random values
        n2=random.randint(0,11)
        #putting the whole question in a single line
        question=int(input(str(n1)+"+"+str(n2)+"="))
        #getting the real answer to see if it matches with the question
        ans=n1+n2
        #checking if the answers match user input
        if question == ans:
            #keeping track of the score
            score = score +1
            update.append(str(n1)+' + '+str(n2)+' = '+str(question)+'(Answer is '+str(ans)+')[Correct]')
        else:
            update.append(str(n1)+' + '+str(n2)+' = '+str(question)+'(Answer is '+str(ans)+')[Incorrect]')

    for val in range(times):
        print(update[val])
            

   
#printing the results
    print()
    print("   Results")
    print("Your name is: ",name)
    print("You played on: easy mode")
    print("You choosen this many questions: ",times)
    print("you have got",score,"/",times,"correct")
    print("your scored : ",(score/times)*100,"/100")
    

#saving the data to a database
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
    sqltxt="INSERT INTO customgameresults (name,difficulty,correct,totalquestions,percentage) VALUES (%s,%s,%s,%s,%s)"
    utxt=(name,"easy",score,times,(score/5)*100)
    cursor.execute(sqltxt,utxt)
#inserting the change
    db.commit()
    
#closing the connection    
    db.close()
    return
    

    

    
