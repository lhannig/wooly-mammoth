import sqlalchemy
import psycopg2

if __name__ == "__main__":

    connection = psycopg2.connect(database='stricken', user='postgres',
                                 password='einoel', host='127.0.0.1')

    cursor = connection.cursor()