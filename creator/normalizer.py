from unicodedata import decimal
from flask import Flask, render_template, flash, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, update, desc
from os import path
from requests import get
from socket import inet_aton
from struct import unpack
from json import loads, dumps

db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = "094JH094I8OTHJ038I94H0PW3HJ4P0OIJHW3P09OHJZ"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

class var():
    clock = 0
    print = 0
    array = []
    with open('credential.txt') as f:
        credential = f.read()

class V4(db.Model):
    decimal_start = db.Column(db.Integer, primary_key=True)
    decimal_end = db.Column(db.Integer, nullable=False)
    ip_start = db.Column(db.String(15))
    ip_end = db.Column(db.String(15))
    lon = db.Column(db.String(20))
    lat = db.Column(db.String(20))
    region = db.Column(db.String(255))
    city = db.Column(db.String(255))
    zip = db.Column(db.String(10))
    asn = db.Column(db.Integer, db.ForeignKey('ASN.id'))
    countryCode = db.Column(db.String(2), db.ForeignKey('COUNTRY.id'))

class COUNTRY(db.Model):
    id = db.Column(db.String(2), primary_key=True)
    name = db.Column(db.String(255))

class ASN(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    isp = db.Column(db.String(255))
    org = db.Column(db.String(255))
    website = db.Column(db.String(255))
    v4 = db.relationship('V4')


if not path.exists('./' + DB_NAME):
    db.create_all(app=app)
    print('Created Database')



@app.route('/')
def create():
    print('start read')
    print('start write')
    ip = V4.query
    for i in ip:
        if i.region == None or not i.region:
            ip = i.ip_start[:-1] + "1"
            answer = get(f'https://ipinfo.io/{ip}?token={var.credential}')
            try:
                i.lon = loads(answer.text)['loc'].split(',')[0]
            except: i.lon = '0'
            try:
                i.lat = loads(answer.text)['loc'].split(',')[1]
            except: i.lat = '0'
            try:
                i.region = loads(answer.text)['region']
            except: i.region = '0'
            try:
                i.city = loads(answer.text)['city']
            except: i.city = '0'
            try:
                i.zip = loads(answer.text)['postal'] 
            except: i.zip = '0'
            try:
                i.countryCode =  loads(answer.text)['country']
            except: i.countryCode = '0'
            try:
                i.name = loads(answer.text)['asn']['name']
            except: i.name = '0'
            try:
                i.isp =  loads(answer.text)['asn']['type']
            except: i.isp = '0'
            try:
                i.org = loads(answer.text)['company']['name']
            except: i.org = '0'
            try:
                i.website = loads(answer.text)['asn']['domain']
            except: i.website = '0'
            db.session.commit()
            r = V4.query.filter_by(ip_start=i.ip_start).first()
            print(r.ip_start, r.lon, r.lat, r.region, r.city, r.zip, r.asn, r.countryCode, r.name, r.isp, r.org, r.website)
        else:
            pass
        
    return f"Fertig"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 