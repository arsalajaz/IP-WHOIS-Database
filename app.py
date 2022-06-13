from unicodedata import decimal
from flask import Flask, render_template, flash, request, url_for, redirect, jsonify
from datetime import timedelta
from flask_mysqldb import MySQL
from os import path
from requests import get
from socket import inet_aton
from struct import unpack
from json import loads, dumps


app = Flask(__name__)
app.config['SECRET_KEY'] = "094JH094I8OTHJ038I94H0PW3HJ4P0OIJHW3P09OHJZ"
app.config['MYSQL_USER'] = 'ip'
app.config['MYSQL_PASSWORD'] = 'TempPass'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'ip'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

mysql = MySQL(app)

@app.route('/<ip>', methods=['GET'])
def notfound(ip):
    return {'request_message':'not_found'}

@app.route('/<ip>', methods=['GET'])
def home(ip):
    return {'request_message':'Visit https://github.com/saschazesiger/IP-WHOIS-Database to learn more about this Service!'}

@app.route('/json/<ip>', methods=['GET'])
def create(ip):
    try:
        result = fetchip(ip)
    except:
        return {'request_message':'invalid_query'}
    return result

def fetchip(ip):
    cur = mysql.connection.cursor()
    ip_decimal = unpack("!L", inet_aton(ip))[0]
    cur.execute(f'''
    SELECT 
        (v4.decimal_end-v4.decimal_start) as ip_range,
        v4.ip_start as ip_rangeStart,
        v4.ip_end as ip_rangeEnd,
        v4.lon as loc_lon,
        v4.lat as loc_lat,
        v4.region as loc_region,
        v4.city as loc_city,
        v4.zip as loc_zip,
        v4.asn as asn_id,
        asn.name as asn_name,
        asn.type as asn_type,
        asn.org as asn_org,
        asn.website as asn_website,
        v4.countryCode as loc_countryCode,
        country.countryCode3 as loc_countryCode3,
        country.countryCode as loc_countryCodeDecimal,
        country.iso as loc_countryCodeIso,
        country.region as loc_countryRegion,
        country.regionCode as loc_countryRegionCode,
        country.subregion as loc_countrySubRegion,
        country.subregionCode as loc_countrySubRegionCode,
        country.language as loc_language,
        country.currencies as loc_currencies,
        country.callingCode as loc_callingCode,
        country.name as loc_countryName
    FROM v4
    LEFT JOIN asn on v4.asn = asn.id
    LEFT JOIN country on v4.countryCode = country.id 
    WHERE v4.decimal_start < {ip_decimal}
    order by v4.decimal_start desc
    limit 1
    ''')
    result = cur.fetchone()
    result.update({'request_message':'success','request_ip':ip,'request_decimal':ip_decimal})
    return result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 