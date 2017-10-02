#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LED Flask
"""

from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, validators


class InputForm(FlaskForm):
    radio = RadioField('LED Status',
                       [validators.Required()],
                       choices=[('on', 'LED on'), ('off', 'LED off')],
                       default='off',
                       )
#    submit = SubmitField("send")
