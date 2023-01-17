from flask import Flask

app = __name__

@app.route('/')
def hello():
    return 'Hello HBNB!'

flask run --host=0.0.0.0

if __name__ == '__main__':
    app.run(debug=True)
