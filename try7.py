import mysql.connector #needed

mydb = mysql.connector.connect(host='vm-test.mscs.mu.edu', user='blackjack2019', password='black_jack_2019',
                                database='blackjack_2019') #needed

cur =mydb.cursor() #needed

def addUser(name):
    cur.execute('INSERT INTO USERS(USERNAME) VALUES (%s)', (name,))
    print('added', name, ' to database')
    mydb.commit()

def deleteUser(name):
    cur.execute('DELETE FROM USERS WHERE USERNAME IN (%s)', (name,))
    print(name, 'is dead')
    mydb.commit()
def fetchData():
    cur.execute("SELECT USERNAME FROM USERS")
    fname = cur.fetchall()
    print(fname)
def pythonUserPromptName():
    name=input("Enter a Username: ")
    return name

def leaderboard():
    'Create leaderboard'
    cur.execute('SELECT USERS.userName AS "User", \
                USERS_SESSIONS.totals AS "Total Games Played", \
                USERS_SESSIONS.winPercentages AS "Win Rate" \
                FROM USERS \
                JOIN USERS_SESSIONS \
                ON USERS.userID = USERS_SESSIONS.userIDs \
                ORDER BY USERS_SESSIONS.winPercentages DESC \
                LIMIT 3')
    fleaderboard = cur.fetchall()
    print(fleaderboard)
    mydb.commit()
    


##Here should be the full Shebang (testing asking, adding, and deleting a user)
leaderboard()
##addUser()
##fetchData()
##deleteUser()
##fetchData()



##This should happen always--Don't delete
cur.close()
mydb.commit()
mydb.close()

## Next Steps:
## Add new user to table - DONE
## Print existing user's record
## Display a leaderboard
## Make this into a method in the main game
## get username from Flask
