# -*- coding: utf-8 -*-
"""
Created on Sat May 14 01:15:18 2022

@author: D
"""
#!/usr/bin/env python3

print("Docker is magic!")
import datetime
import PyMongo
import flask
from flask import request
app = flask.Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/http_server")
db = mongodb_client.db


@app.route("/message",methods=['POST', 'GET'])
def add_one():
    name = request.form.get('name')
    message = request.form.get('message')
    now = str(datetime.datetime.now())
    db.http_server.insert_one({'name': name, 'message': message, 'time': now})
    #return flask.jsonify(message="success")
    return '''
            <form method="POST">
                <div><label>name: <input type="text" name="name"></label></div>
                <div><label>message: <input type="text" name="message"></label></div>
                <input type="submit" value="Submit">
            </form>'''
            
            
            
@app.route("/chat",methods=['GET'])
def load_chat():
    chat = db.http_server.find()
    output = []
    for c in chat:
        output.append({'name' : c['name'], 'message' : c['message'], 'time' : c['time']})
    
    return flask.jsonify(output)































# @app.route("/add_many")
# def add_many():
#     db.todos.insert_many([
#         {'_id': 1, 'title': "todo title one ", 'body': "todo body one "},
#         {'_id': 2, 'title': "todo title two", 'body': "todo body two"},
#         {'_id': 3, 'title': "todo title three", 'body': "todo body three"},
#         {'_id': 4, 'title': "todo title four", 'body': "todo body four"},
#         {'_id': 5, 'title': "todo title five", 'body': "todo body five"},
#         {'_id': 1, 'title': "todo title six", 'body': "todo body six"},
#         ])
#     return flask.jsonify(message="success")



if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run( )
    