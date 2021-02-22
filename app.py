# -*- coding: utf-8 -*-
"""
Created on 21/02/2021 15:40

@author: Akhil

flask wraper for rotate left functionality script - hackerrank_DS_4.py
"""

import os
from flask import Flask
from code import hackerrank_DS_4

app = Flask(__name__)

@app.route("/")
def hrds4():
    page = '<html><body><h1>'
    page += 'Rotating the array to LEFT</h1><div>'
    page += '<input type="text" id="arr-len">' \
            '<br><input type="text" id="shift">' \
            '<br><label for="body" id="desc">space separated list of array members</label>' \
            '<input type="text" id="arr">' \
            '<br><button>Submit</button>' \
            '</div></body></html>'
    return page


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))


