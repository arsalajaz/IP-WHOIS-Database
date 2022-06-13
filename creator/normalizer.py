from unicodedata import decimal
from flask import Flask, render_template, flash, request, url_for, redirect, jsonify
from datetime import timedelta
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




@app.route('/')
def create():
    app.permanent_session_lifetime = timedelta(minutes=1000)
    print('START')
    cur = mysql.connection.cursor()
    num = 0
    clock = 0
    cur.execute(f'''select ip_start, lon from v4''')
    ips = loads(str(cur.fetchall()))
    print(ips)
    for ip in ips:
        if num > clock:
            clock = clock + 1000
            print(clock)
            #mysql.connection.commit()
        num = num + 1
    #mysql.connection.commit()
    return f"Fertig"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 