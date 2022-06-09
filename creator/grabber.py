from unicodedata import decimal
from flask import Flask, render_template, flash, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, update, desc
from os import path
from requests import get
import socket
from struct import unpack
from json import loads, dumps


with open('./ipranges.txt', 'r', encoding="utf-8") as f:
    ipranges = f.read().split('\n')
with open('./ipfull.txt', 'r', encoding="utf-8") as f:
    ipfull = f.read().split('\n')

print('START IP ARRAY')
ipfullarray = []
for ip in ipfull:
    ipfullarray.append(ip.split(',')[0])

print(ipfullarray)
exists = 0
print('START IP LOOKUP')
for ir in ipranges:
    ip = ir.split('\t')[0]
    if ip in ipfullarray:
        exists = exists + 1
    else:
        try:
            ip = ip[:-1] + "1"
            answer = get(f'https://ipinfo.io/{ip}?token=6397916d6dc7fc')
            try:
                lon = loads(answer.text)['loc'].split(',')[0]
            except: lon = '0'
            try:
                lat = loads(answer.text)['loc'].split(',')[1]
            except: lat = '0'
            try:
                region = loads(answer.text)['region']
            except: region = '0'
            try:
                city = loads(answer.text)['city']
            except: city = '0'
            try:
                zip = loads(answer.text)['postal'] 
            except: zip = '0'
            try:
                countryCode =  loads(answer.text)['country']
            except: countryCode = '0'
            try:
                name = loads(answer.text)['asn']['name']
            except: name = '0'
            try:
                isp =  loads(answer.text)['asn']['type']
            except: isp = '0'
            try:
                org = loads(answer.text)['company']['name']
            except: org = '0'
            try:
                website = loads(answer.text)['asn']['domain']
            except: website = '0'

            with open('./ipfull2.txt', 'a', encoding="utf-8") as f:
                f.write(f"{ip},{lon},{lat},{region},{city},{zip},{countryCode},{name},{isp},{org},{website}\n")
            print(f"{ip},{lon},{lat},{region},{city},{zip},{countryCode},{name},{isp},{org},{website}\n")

        except socket.error:        
            print(f'IP not valid: {ip}')

print(exists)
        

