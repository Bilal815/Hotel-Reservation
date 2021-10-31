from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.db'
db = SQLAlchemy(app)

'''Database Model For Storage'''


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, default='N/A')
    gateway = db.Column(db.String(20), nullable=False, default='alipay')
    amount = db.Column(db.Integer, nullable=False, default=0)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_purchased = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='Paid')

    def __repr__(self):
        return 'User ' + str(self.title)



@app.route("/")
def index():
    return "Hi! Hotelier"


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        '''Add entry to the database'''
        name = request.form.get('name')
        amount = request.form.get('amount')
        gateway = request.form.get('gateway')
        payment_time = request.form.get('payment_time')
        created_at = request.form.get('created_at')
        status = request.form.get('status')

        entry = User(title=name, amount=amount, gateway=gateway, date_purchased=payment_time, date_posted=created_at,
                     status=status)
        db.session.add(entry)
        db.session.commit()
        return "form posted!!!"
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
