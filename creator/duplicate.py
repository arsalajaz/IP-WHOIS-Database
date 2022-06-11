from unicodedata import decimal
from flask import Flask, render_template, flash, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, update, desc
from os import path
from requests import get
import socket
from struct import unpack
from json import loads, dumps





with open('./ipfull2.txt', 'r', encoding="utf-8") as f:
    ipfull = f.read().split('\n')

print('STEP 1')


ipfull.sort()

num = 0
gonum = 0
errnum = 0
dupnum = 0
oldip = ""
for ip in ipfull:
    num = num + 1
    try:
        socket.inet_aton(ip.split(',')[0])
        if ip.split(',')[0] == oldip:
            dupnum = dupnum + 1
        else:
            with open('./ipfull.txt', 'a', encoding="utf-8") as f:
                f.write(f"{ip}\n")
            gonum = gonum + 1
        oldip = ip.split(',')[0]
    except socket.error:
        errnum = errnum + 1

print(num, gonum, errnum, dupnum)











