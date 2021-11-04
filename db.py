import mysql.connector
from mysql.connector.fabric.connection import REPORT_ERRORS


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

def view_my_work():
    cursor.execute("SELECT * FROM workstable")
    data = cursor.fetchall() #take all rows and return to a list of tuples
    return data

def view_unique_work():
    cursor.execute("SELECT DISTINCT work FROM workstable")
    data = cursor.fetchall() 
    return data

def get_data(work):
    cursor.execute("SELECT * FROM workstable WHERE work='{}'".format(work))
    data = cursor.fetchall() 
    return data

def update_data(new_work, new_work_status, new_work_due_date, work, work_status, work_due_date):
    cursor.execute("UPDATE workstable SET work=?, work_status=?, work_due_date=? WHERE work=? and work_status=? and work_due_date=?", (new_work, new_work_status, new_work_due_date, work, work_status, work_due_date))
    conn.commit()
    data = cursor.fetchall() 
    return data