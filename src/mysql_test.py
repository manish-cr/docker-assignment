from flask import Flask, request, render_template, redirect, jsonify
import pandas as pd
import mysql.connector

def establish_sql_connection():
    try:
        db = mysql.connector.connect(
            host='db',
            user='root',
            password='dsa3101_student',
            database='SOLACE_TRUST'
        )
        return db
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None

def customers():
    db = establish_sql_connection()
    cursor = db.cursor()
    query = "SELECT *\
        FROM customers\
            ORDER BY customer_id DESC"
    cursor.execute(query)
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=['ID','Name','Age','Gender', 'Income',
                                       'Account Duration', 'Segment', 'Credit Score', 
                                       'Address'])
    
    cursor.close()
    db.close()

    return render_template(
        'customers.html', users = df.to_html(index=False)
    )

customers()