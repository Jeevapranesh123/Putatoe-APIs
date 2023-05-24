import mysql.connector
import os 

from dotenv import load_dotenv
load_dotenv()

print(os.getenv('DB_HOST'), os.getenv('DB_USER'), os.getenv('DB_PASSWORD'), os.getenv('DB_NAME'))


mydb = mysql.connector.connect(
  host=os.getenv('DB_HOST'),
  user=os.getenv('DB_USER'),
  password=os.getenv('DB_PASSWORD'),
  database=os.getenv('DB_NAME')
)

mycursor = mydb.cursor()

def insert(table, word):
    data = get(table)
    print(len(data))

    if len(data) == 1 and data[0][1] == word:
        return True
    
    if len(data) == 1 and data[0][1] != word:
        sql = "DELETE FROM {} WHERE word = '{}'".format(table, data[0][1])
        mycursor.execute(sql)
        mydb.commit()


        sql = "INSERT INTO " + table + " (word) VALUES (%s)"
        val = (word,)
        mycursor.execute(sql, val)
        mydb.commit()

        return True
    
    if len(data) > 1:
        for x in data:
            if word == x[1]:
                found = True
            elif word != x[1]:
                sql = "DELETE FROM {} WHERE word = '{}'".format(table, x[1])
                mycursor.execute(sql)
                mydb.commit()

        if found == False:
            sql = "INSERT INTO " + table + " (word) VALUES (%s)"
            val = (word,)
            mycursor.execute(sql, val)
            mydb.commit()

            return True


def get(table):
    mycursor.execute("SELECT * FROM " + table)
    myresult = mycursor.fetchall()
    return myresult

