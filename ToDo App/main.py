from flask import Flask, render_template
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

    def __repr__(self):
        return f"{self.sno}-{self.title}--{self.desc}--{self.date_created}"

@app.route("/")
def hello_world():
    db.session.add(Todo(title="Start working on flask",
                        desc="We need to work on seting up sqlalchemy for flask application and learn he orm"
                        ))
    db.session.commit()
    todos = db.session.execute(db.select(Todo).order_by(Todo.date_created)).all()

    return render_template('index.html', todos=todos)




@app.route('/products')
def products():
    return 'this is products page'


if __name__ == "__main__":

    app.run(debug=True)

