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
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

mysql = MySQL(app)




@app.route('/json/<ip>')
def create(ip):
    result = fetchip(ip)
    return result

def fetchip(ip):
    cur = mysql.connection.cursor()
    ip_decimal = unpack("!L", inet_aton(ip))[0]
    cur.execute(f'''
    SELECT 
        v4.decimal_start,
        v4.decimal_end,
        v4.ip_start,
        v4.ip_end,
        v4.lon,
        v4.lat,
        v4.region,
        v4.city,
        v4.zip,
        v4.asn,
        asn.name,
        asn.type,
        asn.org,
        asn.website,
        v4.countryCode,
        country.countryCode3,
        country.countryCode,
        country.iso,
        country.region,
        country.regionCode,
        country.subregion,
        country.subregionCode,
        country.language,
        country.currencies,
        country.callingCode,
        country.name
    FROM v4
    LEFT JOIN asn on v4.asn = asn.id
    LEFT JOIN country on v4.countryCode = country.id 
    WHERE v4.decimal_start < {ip_decimal}
    order by v4.decimal_start desc
    limit 1
    ''')
    result = cur.fetchone()
    return result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 