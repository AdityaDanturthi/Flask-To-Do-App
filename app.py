from datetime import datetime
from urllib import request
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db' # three forward slashes is a relative path and four is for absolute path
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    content = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Integer, default = 0)
    dateCreated = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        taskContent = request.form['content']
        newTask = Todo(content = taskContent)

        try:
            db.session.add(newTask)
            db.session.commit()
            return redirect('/')
        
        except:
            return ' There was an issue adding your task!'
    else:
        tasks = Todo.query.order_by(Todo.dateCreated).all()
    return render_template('index.html', tasks = tasks)

@app.route('/delete/<int:id>')
def delete(id):
    tasktodelete = Todo.query.get_or_404(id)

    try:
      db.session.delete(tasktodelete)
      db.session.commit()
      return redirect('/')

    except:
        return 'There was an issue deleting the task!'  

@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        
        except:
            return 'There was an issue updating the task!'
    else:
        return render_template('update.html', task = task)


if __name__ == "__main__":
    app.run(debug = True)