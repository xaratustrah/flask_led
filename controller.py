#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Raspberry Pi LED Flask

"""
from model import InputForm
from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
#from bokeh.resources import INLINE
from flask_wtf.csrf import CSRFProtect

import os
RASPI = False
# armv6l for Raspberry Pi Zero, armv7l for Raspberry Pi 3
if os.name == 'posix' and (os.uname().machine == 'armv6l' or os.uname().machine == 'armv7l'):
    RASPI = True
    try:
        from engine import Engine
    except RuntimeError:
        print('Missing sudo?')

app = Flask(__name__)
app.secret_key = 'shhhhhhh!'

CSRFProtect(app)
Bootstrap(app)


@app.route('/_radio_update', methods=['GET', 'POST'])
def _radio_update(ledstatus):
    print(ledstatus)


@app.route('/', methods=['GET', 'POST'])
def index():
    if RASPI:
        engine = Engine()

    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        ledstatus = request.form['radio']
        if ledstatus == 'on':
            print(ledstatus, RASPI)
            if RASPI:
                engine.turn_on()
        else:
            print(ledstatus, RASPI)
            if RASPI:
                engine.turn_off()
    return render_template('view.html', form=form,)


# ------
if __name__ == '__main__':
    print(RASPI)
    app.run(debug=True)
