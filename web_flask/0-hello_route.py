#!/usr/bin/python3
""" starts a flask web applications"""
from flask import Flask

app = Falsk(__name__)

@app.route('/')
def hello():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
