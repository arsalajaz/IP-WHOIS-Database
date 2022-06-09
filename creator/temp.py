from unicodedata import decimal
from flask import Flask, render_template, flash, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, update, desc
from os import path
from requests import get
import socket
from struct import unpack
from json import loads, dumps



with open('./ipfull.txt', 'r', encoding="utf-8") as f:
    ipfull = f.read().split('\n')

number = 0
print('START IP ARRAY')
ipfullarray = []
for ip in ipfull:
    number = number + 1
    try:
        array = ip.split(',')
        if array[1] == '0':
            pass
        with open('./ipfull2.txt', 'a', encoding="utf-8") as f:
            f.write(f"{ip}\n")
    except:
        print(f'ERROR {number}: {ip}')





