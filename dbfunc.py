import psycopg2
from configdb import config

def connect():
    """
    connecting to the database server
    """

    conn = None 
    try:
        # reading the parameters from configdb
        params = config()

        # connecting to server
        print("connecting to db...")
        # use the driver psycopg2 function connect with kwargs(**params) to accept the output of configdb
        conn = psycopg2.connect(**params)

        # creating a pointer to will allow interaction with the db
        sat = conn.cursor()

        # executing statemenrs
        print("First prompt - database version")
        sat.execute('select version();')

        # display the output of the statement
        db_version = sat.fetchone()
        print(db_version)

        # close communication with the cusor
        sat.close()

    # if connection and statement execution fails
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    # if a connection is made remember to close connection
    finally:
        if conn != None:
            # close communication with the cusor/pointer
            conn.close()
            print('connection to db is closed')

# if this file is called execute connect
if __name__ == '__main__':
    connect()
