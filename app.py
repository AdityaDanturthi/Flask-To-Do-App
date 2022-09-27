from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db' # three forward slashes is a relative path and four is for absolute path
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    task = db.Column(db.String(200), nullable = False)
    dateCreated = db.Column(db.DateTime, default = datetime.utcnow)

def __repr__(self):
    return '<Task %r>' % self.id

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)