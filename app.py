# app.py

from flask import Flask, render_template, redirect, url_for, jsonify, request
from talk_mashup_bot import talk_mashup_bot

app = Flask(__name__)

@app.route('/')
def hello():
    #return "Hello world!"
    return "Bye Bye Bye"

@app.route('/talk/new')
def new_talk():
    #return "An ALA conference title mashup will be here!"    
    talk_title = talk_mashup_bot.generateTitle()
    return talk_title

if __name__ == '__main__':
    app.run(debug=True)