#!/bin/py

import sqlite3
from flask import Flask, render_template
import hashlib

app = Flask(__name__)
login_info = logininfo.csv

@app.route('/')
def index():
    render_template('index.html')

@app.route('/login')
def login():
    if hashlib.sha256(input_username.encode('utf-8')).hexdigest() == 
    with open('login_info', mode='r') as login_file:
        csvFILE = csv.reader(login_file)
        for lines in csvFILE:

@app.route('/admin')
def admin():
    
            

if __name__ == '__main__':
    app.run()