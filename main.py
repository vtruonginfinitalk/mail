# -*- coding: utf-8 -*-
__author__ = 'nobita'
import os

from flask import Flask, request
from mail_process import extract_mail
app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

@app.route('/', methods = ['GET'])
def homepage():
    return app.send_static_file('index.html')


@app.route('/ner', methods=['POST'])
def process_request():
    data = request.form['data']
    print(u'Input:\n%s' % (data))
    result = extract_mail(data)
    print(u'Result:\n%s' % (result))
    return result



if __name__ == '__main__':


    ON_HEROKU = os.environ.get('ON_HEROKU')

    if ON_HEROKU:
        # get the heroku port
        port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
    else:
        port = 5000
    app.run('0.0.0.0', port=port)