from unicodedata import decimal
from flask import Flask, render_template, flash, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, update, desc
from os import path
from requests import get
from socket import inet_aton
from struct import unpack

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
    go()
    print('start write')
    db.session.commit()
    print('finish')
    return 'finish'


def go():
    with open('./raw/ip2asn-v4.tsv', 'r') as f:
        var.raw = f.read().split('\n')

    for i in var.raw:
        try:
            var.asn = i.split('\t')[2]
        except Exception as e:
            print(f"ERROR on {i}: {e}")
        if var.asn not in var.array:
            var.array.append(var.asn)
        var.clock = var.clock + 1
        if var.clock > var.print:
            print(var.print)
            var.print = var.print + 10000
    print('appending')
    for i in var.array:
            db.session.add(i)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 