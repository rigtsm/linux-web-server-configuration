#!/usr/bin/python3
import psycopg2

from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None

    try:
        # read connection parameters
        params = config()
        #print(params)

        # connecting to PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        print("Conn cursor")
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('Select version()')

        # display the PostgresSql database version
        db_version = cur.fetchone()
        print(db_version)

        #close the **communication** with Postgresql
        cur.close()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')        


if __name__ == '__main__':
    connect()