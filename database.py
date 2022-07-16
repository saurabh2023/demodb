from sqlite3 import Cursor
import sql.connector

config = {
    'user':'root',
    'password':'',
    'host':'localhost'
}

db = mysql.connector.connect(**config)

cursor = db.cursor()