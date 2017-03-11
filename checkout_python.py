import sqlite3

def create_database(db_name):
    connection = sqlite3.connect(db_name)
    print ("Database" + db_name + "opened!")
    connection.execute( '''CREATE TABLE USERS
                        (ID         INTEGER PRIMARY KEY AUTOINCREMENT,
                        USERNAME    TEXT        NOT NULL,
                        PASSWORD    TEXT        NOT NULL,
                        FIRSTNAME   TEXT        NOT NULL,
                        LASTNAME    TEXT        NOT NULL,
                        ADDRESS     CHAR(50)    NOT NULL,
                        CARDNUM     INT         NOT NULL,
                        CARDMAKER   TEXT        NOT NULL);''')
def insert_database(db_name, username, password, first, last, address, cardnum, cardmaker):
    #connection = sqlite3.connect(db_name)
    id_query = connection.execute("Select MAX(ID) FROM USERS")
    for row in id_query:
        max_id = row[0] + 1
    connection.execute("INSERT INTO USERS VALUES (?,?,?,?,?,?,?,?)",[max_id,username, password, first, last, address, cardnum, cardmaker])
    connection.commit()
    #connection.close()
def query_database(db_name, username, password):
    #connection=sqlite3.connect(db_name)
    query = []
    query = connection.execute("SELECT * FROM USERS WHERE USERNAME = (?) AND PASSWORD = (?)", [username, password])
    #connection.close()
    return query
connection = sqlite3.connect('supreme')
loop = 1
while(loop == 1):
    print "Press 1 to add a user"
    print "Press 2 to load a user"
    print "Press 3 to purchase"
    print "Press 4 to quit"
    option = input("Select an option: ")
    if option == 1:
        username        =   raw_input("Enter a username: ")
        password        =   raw_input("Enter a password: ")
        first           =   raw_input("Enter first name: ")
        last            =   raw_input("Enter last name: ")
        card_number     =   raw_input("Enter credit card number: ")
        card_maker      =   raw_input("Enter credit card maker: ")
        address         =   raw_input("Enter address: ")
        insert_database("supreme", username, password, first, last, address, card_number, card_maker)
    if option == 2:
        username        =   raw_input("Enter username: ")
        password        =   raw_input("Enter password: ")
        user = query_database("supreme", username, password)
        for i in user:
            user_load = str(i[1])
            first_load = str(i[3])
            last_load = str(i[4])
            address_load = str(i[5])
            card_load = str(i[6])
            card_maker_load = str(i[7])
    if option == 3:
        selected_item = "Work on"
    if option == 4:
        loop = 0
    if option == 404:
        create_database("supreme")
quit()
