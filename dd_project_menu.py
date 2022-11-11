#Thomas O'Brien R00192530
#Database Deisgn project code
import mysql.connector

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password ='root',
    database ="mydatabase"
)
#Creating database
#mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")

#Creating table
#mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE PlayerData ( Fname VARCHAR(255), Lname VARCHAR(255),
#  Country  VARCHAR(255), Club  VARCHAR(255), JerseyNo int, Position  VARCHAR(255), GoalsScored  int, primary key(JerseyNo));")
#mydb.commit()

#code to show table to see if the table was successfully created or not
#mycursor = mydb.cursor()

#mycursor.execute("show tables")

#for x in mycursor:
#  print(x)

#while project is true it will run 
while True:
    try:
        #print staements to make up the menu
        print("Database Menu")
        print("==============================")
        print("1: insert data to the database")
        print("2: update the data in the database")
        print("3: display the data in the database")
        print("4: Delete data stored in the database")
        print("5: Exit program")
        #input which takes a value from 1-5 and carries out a task depending on which using if-elif statements
        option = int(input(">>> "))
        #if the user wants to insert a new player to the database
        if option == 1:
            print("Insert Data")
            print("============")
            #input statements which record each attribute to be stored in the database table
            Fname = input("Enter Fname > ")
            Lname = input("Enter Lname > ")
            Country = input("Enter Country > ")
            Club = input("Enter Club > ")
            JerseyNo = int(input("Enter JerseyNo > "))
            Position = input("Enter Position > ")
            GoalsScored = int(input("enter No of goals scored > "))

            #create a new cursor and assign under the variable data
            data = mydb.cursor()
            #sql statement that is to be executed i used %s as a prevention measure from sql injection for good security practice 
            #i used a insert statement to add the data to the database table 
            SQLinsertdata = "insert into PlayerData (Fname, Lname, Country, club, JerseyNo, Position, GoalsScored) values (%s, %s, %s, %s, %s, %s, %s)"
            #each of these values is represented by a %s in the order below
            values = (Fname, Lname, Country, Club, JerseyNo, Position, GoalsScored)
            #executes the sql statement and the input values
            data.execute(SQLinsertdata, values)
            #this is needed to commit the changes to the database
            mydb.commit()
            #print statements which shows if the data was successfully altered and how many rows were affected
            print(data.rowcount, "record of player info added")


            
            #when the user wants to update existing 
        elif option == 2:
            
            print("Upate Data")
            print("==============")
            #1=Fname, 2=Lname, 3=Country, 4=Club, 5=Position, 6=GoalsScored
            updatedata = int(input("select table value to update[1,2,3,4,5,6] > "))
            #user wants to update a players First name
            if updatedata == 1:
                #input statement to get new name
                updatevariable = input("enter new plyer name > ")
                #user enters the players jerseyno to be used as a primary key to link the right player to have thier name changed
                jersey = int(input("Enter player jersey no > "))
                #create a new cursor and assign under the variable data
                data = mydb.cursor()
                #i used the update stetement with jerseyno as the primary key to link the data
                SQLinsertdata = "update playerdata set Fname = %s where JerseyNo = %s"
                 #each of these values is represented by a %s in the order below
                values = (updatevariable, jersey)
                 #executes the sql statement and the input values
                data.execute(SQLinsertdata, values)
                #this is needed to commit the changes to the database
                mydb.commit()
                #print statements which shows if the data was successfully altered and how many rows were affected
                print(data.rowcount, "row(s) affected")

            #the rest of these elif statements are the same in operation just correspong the piece of data that they will change
            elif updatedata == 2:
                updatevariable = input("enter new surname > ")
                jersey = int(input("Enter player jersey no > "))
                data = mydb.cursor()
                SQLinsertdata = "update playerdata set Lname = %s where JerseyNo = %s"
                values = (updatevariable, jersey)
                data.execute(SQLinsertdata, values)
                mydb.commit()
                print(data.rowcount, " row(s) affected")
            elif updatedata == 3:
                updatevariable = input("enter new country > ")
                jersey = int(input("Enter player jersey no > "))
                data = mydb.cursor()
                SQLinsertdata = "update playerdata set Country = %s where JerseyNo = %s"
                values = (updatevariable, jersey)
                data.execute(SQLinsertdata, values)
                mydb.commit()
                print(data.rowcount," row(s) affected")
            elif updatedata == 4:
                updatevariable = input("enter new club > ")
                jersey = int(input("Enter player jersey no > "))
                data = mydb.cursor()
                SQLinsertdata = "update playerdata set Club = %s where JerseyNo = %s"
                values = (updatevariable, jersey)
                data.execute(SQLinsertdata, values)
                mydb.commit()
                print(data.rowcount, " row(s) affected")
            elif updatedata == 5:
                updatevariable = input("enter new player position > ")
                jersey = int(input("Enter player jersey no > "))
                data = mydb.cursor()
                SQLinsertdata = "update playerdata set Position = %s where JerseyNo = %s"
                values = (updatevariable, jersey)
                data.execute(SQLinsertdata, values)
                mydb.commit()
                print(data.rowcount, " row(s) affected")
            elif updatedata == 6:
                updatevariable = int(input("enter new data no of goals scored > "))
                jersey = int(input("Enter player jersey no > "))
                data = mydb.cursor()
                SQLinsertdata = "update playerdata set GoalsScored = %s where JerseyNo = %s"
                values = (updatevariable, jersey)
                data.execute(SQLinsertdata, values)
                mydb.commit()
                print(data.rowcount, " row(s) affected")
            #in the event the user enters a string or the wrong number
            else:
                print('wrong input')
        #if the user wants to display the data stored in the database stored as rows
        elif option == 3:
            print("Display Rows")
            print("==============")
            #create a new cursor and assign under the variable data
            data = mydb.cursor()
            #executes the sql statement and the input values
            #i used select * to display all data stored in the database
            data.execute("select * from playerdata")
            #use fetchall function to grab all the data stored in the table
            result = data.fetchall()
            #for statement that will print the data to the console
            for x in result:
                print(x)
        #if the user wants to delete one of the players from the database
        elif option == 4:
                print("Delete Data")
                print("==============")
                 #input statement to get new name
                deletevariable = input("enter player name to delete > ")
                 #user enters the players jerseyno to be used as a primary key
                jersey = int(input("Enter player jersey no > "))
                #create a new cursor and assign under the variable data
                data = mydb.cursor()
                 #i used the delete from stetement with jerseyno as the primary key to link the data
                SQLinsertdata = "delete from playerdata where Fname = %s and JerseyNo = %s"
                 #each of these values is represented by a %s in the order below
                Fnamevalue = (deletevariable, jersey)
                 #executes the sql statement and the input values
                data.execute(SQLinsertdata, Fnamevalue)
                #this is needed to commit the changes to the database
                mydb.commit()
                #print statements which shows if the data was successfully altered and how many rows were deleted
                print(data.rowcount, "row(s) deleted")
           
           
        #if the user wants to exit the program
        elif option == 5:
            break
        #if the user dosent select an option from 1-5
        else:
            print('wrong input')
     #used to catch any errors from mistyping in input statements and other stuff also
    except ValueError:
        print('exception')