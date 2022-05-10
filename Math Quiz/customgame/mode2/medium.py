def med():
    import random
    #variables
    score=0
    rand=0
    update=[]
    #creating list with the operators in them
    op=["+","-"]
    name=str(input("Enter name: "))
    times=int(input("How many questions would you like? = "))
    print()
    #main program
    for i in range(times):
        n1=random.randint(0,51)#importing 2 random values
        n2=random.randint(0,51)
        operators=random.choice(op)# used to chooose a random value from the "op"
        #putting the whole question in a single line
        question=int(input(str(n1)+str(operators)+str(n2)+"="))
        #getting the real answer to see if random operator is "+"
        if(operators == "+"):
            ans=n1+n2
        #getting the real answer to see if random operator is "-"
        if(operators == "-"):
            ans=n1-n2
        #checking if the answers match user input
        if question == ans:
            #keeping track of the score
            score = score +1
            update.append(str(n1)+str(operators)+str(n2)+' = '+str(question)+'(Answer is '+str(ans)+')[Correct]')
        else:
            update.append(str(n1)+str(operators)+str(n2)+' = '+str(question)+'(Answer is '+str(ans)+')[Incorrect]')

    for val in range(times):
        print(update[val])


#printin the results
    print()
    print("   Results")
    print("Your name is: ",name)
    print("You played on: medium mode")
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
    utxt=(name,"medium",score,times,(score/5)*100)
    cursor.execute(sqltxt,utxt)
#inserting the change
    db.commit()
   
#closing the connection    
    db.close()
    return
  
