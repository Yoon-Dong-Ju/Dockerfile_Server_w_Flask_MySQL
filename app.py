from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask_user:flask_password@db/flask_db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello, Dockerized Flask App with MySQL!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
