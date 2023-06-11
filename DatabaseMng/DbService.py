
import pymysql
from DbUtil import DbUtil

def connect():
    conn = pymysql.connect(host='localhost',
                           user='research',
                           password='123456',
                           db='world',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    return conn, cursor

try:
    conn, cursor = connect()

    conn.commit()
finally:
    conn.close()