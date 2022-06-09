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

print('START IP ARRAY')
ipfullarray = []
for ip in ipfull:
    part1 = ip.split(',')[0][:-1] + "0"
    part2 = ip.replace(ip.split(',')[0], "")
    with open('./ipfull3.txt', 'a', encoding="utf-8") as f:
        f.write(f'{part1}{part2}\n')



