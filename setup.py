import mysql.connector
from mysql.connector import error
from database import cursor

DB_NAME = 'SA'

TABLES = {}

TABLES["logs"] = (
    "CREATE TABLE `logs` ("
    "`id` int(12) NOT NULL AUTO_INCREMENT",
    "`text` varchar(250) NOT NULL",
    "`user` varchar(250) NOT NULL",
    "`created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP",
    "PRIMARY KEY(`id`)",
    ") ENGINE=InnoDB"
)

def create_db():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("DATABASE {} CREATED!".format(DB_NAME))

def create_tables():
    cursor.execute("USE {}".format(DB_NAME))

    for tabel_name in TABLES:
        tabel_description = TABLES[tabel_name]
        try:
            print("Creating table ({})".format(table_name), end='')
            cursor.execute(tabel_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already exists")
            
create_db()

create_tables()

# acjancjac