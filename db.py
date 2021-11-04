# from app import landpage
import mysql.connector


conn = mysql.connector.connect( host="localhost",
                                port="3306",
                                user="root",
                                passwd="",
                                db="crud"
                              )
cursor = conn.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS workstable(work TEXT, work_status TEXT, work_due_date DATE)")

def create_data(work, work_status, work_due_date):
    cursor.execute("INSERT INTO workstable(work, work_status, work_due_date) VALUES (%s,%s,%s)", (work, work_status, work_due_date))
    conn.commit()

