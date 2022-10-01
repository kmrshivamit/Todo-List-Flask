from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Shivam11@localhost/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # def __repr__(self):
    #     return f"{self.sno}-{self.title}--{self.desc}--{self.date_created}"


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        if request.method == "POST":
            todo = Todo(
                title=request.form["title"],
                desc=request.form["desc"]
            )
            db.session.add(todo)
            db.session.commit()

    todos = db.session.execute(db.select(Todo).order_by(Todo.date_created)).scalars()

    return render_template('index.html', todos=todos)


@app.route('/products')
def products():
    return 'this is products page'


if __name__ == "__main__":
    app.run(debug=True)
