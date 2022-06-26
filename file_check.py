from flask import *
from flask import request

from bson.objectid import ObjectId
import base64
import os

file_check = Flask('hacks')

@file_check.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        document={}
        #print('here')
        for item in request.form:
            #print(item)
            document[item]=request.form[item]
            with open('myfile.json', 'w', encoding='utf8') as json_file:
                json_object = json.dump(document, json_file)
        return "done"

if __name__ == '__main__':
    file_check.run(debug=True)