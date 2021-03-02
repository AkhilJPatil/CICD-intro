# -*- coding: utf-8 -*-
"""
Created on 21/02/2021 15:40

@author: Akhil

flask wraper for rotate left functionality script - hackerrank_DS_4.py
"""

import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from code import hackerrank_DS_4
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)

class Rotations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_arr = db.Column(db.String(1000), nullable=False)
    rotation_by = db.Column(db.Integer, nullable=False)
    rotation_direction = db.Column(db.String(20), nullable=False)
    op_arr = db.Column(db.String(1000), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Rotation %r>' % self.id


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            shift = int(request.form['shift'])
            arr = request.form['arr']
            arr = list(map(int, arr.rstrip().split()))
            direction = ''

            if request.form.get("btn_rot_lf"):
                res = hackerrank_DS_4.rotateLeft(shift, arr)
                direction = 'left'

            else:  # request.form.get("btn_rot_rt"):
                res = hackerrank_DS_4.rotateRight(shift, arr)
                direction = 'right'

            # storing record to DB
            new_entry = Rotations(ip_arr=str(arr),
                                  rotation_by=shift,
                                  rotation_direction=direction,
                                  op_arr=str(res))
            db.session.add(new_entry)
            db.session.commit()

            # fetching all records from DB
            recs = Rotations.query.order_by(Rotations.date).all()

            return render_template('output.html', res=str(res), recs=recs)

        except Exception as e:
            return render_template('404.html', err="Error "+str(e))
        # return redirect('/')
    else:
        return render_template('index.html')


@app.route("/output/", methods=['GET'])
def back():
    try:
        return redirect("/")
    except Exception as e:
        return str(e)


# @app.route("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=False)


