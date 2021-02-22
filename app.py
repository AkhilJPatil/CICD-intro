# -*- coding: utf-8 -*-
"""
Created on 21/02/2021 15:40

@author: Akhil

flask wraper for rotate left functionality script - hackerrank_DS_4.py
"""

import os
from flask import Flask, render_template, request, redirect
from code import hackerrank_DS_4

app = Flask(__name__)

# class model():


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        shift = request.form['shift']
        arr = request.form['arr']
        try:
            arr = list(map(int, arr.rstrip().split()))
            res = hackerrank_DS_4.rotateLeft(int(shift), arr)
            return render_template('output.html', res=str(res))
        except Exception as e:
            return "Error "+str(e)
        # return redirect('/')
    else:
        return render_template('index.html')


@app.route("/output/", methods=['GET'])
def back():
    try:
        return redirect("/")
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=False)


