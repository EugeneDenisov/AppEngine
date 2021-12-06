from flask import Flask
from random import randint
#from google.cloud import storage
import os
#from datetime import datetime

app = Flask(__name__)


@app.route('/')
def starting_page():
    return 'Greetings my friend!'


@app.route('/get-item')
def get_number():
#    now = datetime.now()
#    dt_string = now.strftime("%d-%m-%Y-%H:%M:%S")
#    path = os.path.abspath(os.getcwd())
#    client = storage.Client.from_service_account_json(os.getenv("GOOGLE_APPLICATION_CREDENTIALS","n/a"))
#    client = storage.Client()
#    bucket = client.get_bucket('flask-app-logs')
#    blob = storage.Blob(dt_string + '.txt', bucket)
    if os.getenv("NUMBER_TYPE") == "all":
        n = randint(0,1000)
        with open(path + "/archive/output.txt","a+") as fl:
            fl.write(str(n) + " all \n")
        fl.close()
#        blob.upload_from_filename(path + '/archive/output.txt')
        return str(n) + " all"
    elif os.getenv("NUMBER_TYPE") == "odd":
        n = randint(0,500)*2 - 1
        path = os.path.abspath(os.getcwd())
        with open(path + "/archive/output.txt","a+") as fl:
            fl.write(str(n) + " odd \n")
        fl.close()
#        blob.upload_from_filename(path + '/archive/output.txt')
        return str(n) + " odd"
    elif os.getenv("NUMBER_TYPE") == "even":
        n = randint(0,500)*2
        path = os.path.abspath(os.getcwd())
        with open(path + "/archive/output.txt","a+") as fl:
            fl.write(str(n) + " even \n")
        fl.close()
#        blob.upload_from_filename(path + '/archive/output.txt')
        return str(n) + " even"
    else:
        return "Wrong NUMBER_TYPE"


@app.route('/author')
def author():
#    return os.getenv("fullName","n/a") + "<br/>" + os.getenv("MY_NODE_NAME","n/a") + "<br/>" + os.getenv("MY_POD_NAME","n/a")
    return "Yauheni Dzianisau"

if __name__ == '__main__':
    print("v2.8")
    app.run(debug=True)
