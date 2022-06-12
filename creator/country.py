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
    with open('./creator/raw/country.csv', 'r', encoding='utf-8') as f:
        ips = f.read().split('\n')
    app.permanent_session_lifetime = timedelta(minutes=60)
    print('START')
    cur = mysql.connection.cursor()
    num = 0
    clock = 0
    for ip in ips:
        array = ip.split(',')
        try:
            cur.execute(f'''INSERT INTO country(id, countryCode3, countryCode, iso, name, region, regionCode, subregion, subregionCode) VALUES ("{array[1]}","{array[2]}",{array[3]},"{array[4]}","{array[0]}","{array[5]}",{array[8]},"{array[6]}",{array[9]})''')
            mysql.connection.commit()
        except Exception as e:
            if 'Duplicate entry' not in f"{e}":
                print(f'ERROR: {e} at {array}')

    mysql.connection.commit()
    return f"Fertig"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 