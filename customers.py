###########################################
#### DO NOT REMOVE THE FUNCTIONS BELOW ####
###########################################

from flask import Flask, request, render_template, redirect, jsonify
import pandas as pd
import mysql.connector

app = Flask(__name__)
get_defaults = { 'gender': 'Female', 
                 'segment': 'Regular', 
                 'limit': 10 
                 }

def establish_sql_connection():
    db = mysql.connector.connect(
    host="db",
    user="root",
    password="dsa3101_student",
    database="SOLACE_TRUST"
    )
    return db

@app.route("/")
def home():
    return render_template(
        'home.html'
    )

@app.route("/customers")
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

@app.route("/get_customers_gender_segment", methods=["GET"])
def customers_gender_segment():
    gender = request.args.get('gender', get_defaults['gender'])
    segment = request.args.get('segment', get_defaults['segment'])
    limit = request.args.get('limit', get_defaults['limit'])

    db = establish_sql_connection()
    cursor = db.cursor()
    #### ADD YOUR SQL QUERY BELOW ####
    query=f"SELECT * FROM\
        customers WHERE customer_gender='{gender}'\
            AND customer_segment='{segment}'\
                ORDER BY customer_id DESC\
                    LIMIT {limit}"

    cursor.execute(query)
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=['ID','Name','Age','Gender', 'Income',
                                       'Account Duration', 'Segment', 'Credit Score', 
                                       'Address'])
    
    cursor.close()
    db.close()

    return jsonify(df.to_json(orient="records", index=False))

@app.route("/add_customer", methods=["POST"])
def add_customer():
    customer_id = request.form['customer_id']
    customer_name = request.form['customer_name']
    customer_age = request.form['customer_age']
    customer_gender = request.form['customer_gender']
    customer_income = request.form['customer_income']
    customer_account = 1 # starting account is 1
    customer_segment = request.form['customer_segment']
    customer_credit_score = request.form['customer_credit_score']
    customer_address = request.form['customer_address']

    db = establish_sql_connection()
    cursor = db.cursor()

    query = f"\
        INSERT INTO customers\
        (customer_id, customer_name, customer_age, customer_gender, customer_income,\
            customer_account, customer_segment, customer_credit_score,\
            customer_address)\
        VALUES ({customer_id}, '{customer_name}', {customer_age}, '{customer_gender}',\
            {customer_income}, {customer_account},'{customer_segment}',\
            {customer_credit_score}, '{customer_address}')\
    "

    cursor.execute(query)
    db.commit()

    cursor.close()
    db.close()

    return f"Record {customer_id} has been added."

@app.route("/delete_customer", methods=["DELETE"])
def delete_customer():
    customer_id = int(request.get_json()['customer_id'])

    db = establish_sql_connection()
    cursor = db.cursor()

    #### ADD YOUR SQL QUERY BELOW ####
    query = f"\
    DELETE FROM customers\
        WHERE customer_id={customer_id}\
    "

    cursor.execute(query)
    db.commit()

    cursor.close()
    db.close()

    return f"Record {customer_id} deleted."


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000", debug=True)
