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

with open('./creator/ipfull.txt', 'r', encoding='utf-8') as f:
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
            cur.execute(f'''UPDATE v4 set lon = {array[1]}, lat = {array[2]}, region = {array[3]}, city = {array[4]}, zip = {array[5]} ''')
            mysql.connection.commit()
            print(f"lon = {array[1]}, lat = {array[2]}, region = {array[3]}, city = {array[4]}, zip = {array[5]}")
        except Exception as e:
            print(e)
    return f"Fertig"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 