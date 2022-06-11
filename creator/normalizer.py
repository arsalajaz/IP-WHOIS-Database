from unicodedata import decimal
from flask import Flask, render_template, flash, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL
from sqlalchemy import func, update, desc
from os import path
from requests import get
from socket import inet_aton
from struct import unpack
from json import loads, dumps


app = Flask(__name__)
app.config['SECRET_KEY'] = "094JH094I8OTHJ038I94H0PW3HJ4P0OIJHW3P09OHJZ"
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'ip'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

with open('./creator/raw/ip.csv', 'r') as f:
    ips = f.read().split('\n')

class var():
    clock = 0
    print = 0
    array = []

@app.route('/')
def create():
    cur = mysql.connection.cursor()
    for ip in ips:
        array = ip.split(',')
        try:
            cur.execute(f'''INSERT INTO v4(decimal_start,decimal_end,ip_start,ip_end,asn,countryCode) VALUES ({array[0]},{array[1]},"{array[2]}","{array[3]}",{array[9]},"{array[10]}")''')
            mysql.connection.commit()
            print(f"{array[0]},{array[1]},{array[2]},{array[3]},{array[9]},{array[10]}")
        except Exception as e:
            print(e)
    return f"Fertig"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 