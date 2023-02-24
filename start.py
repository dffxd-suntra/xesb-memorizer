from bottle import route, post, run, static_file, request, response, abort
import json
import re
import os

def noCors():
    response.set_header("Access-Control-Allow-Origin", "*")
    response.set_header("Access-Control-Allow-Headers", "*")
    response.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS, DELETE, PUT")

def readConfig():
    file = open("config.json", encoding="utf-8")
    return json.loads(file.read())


""" def checkUser(user, password):
    return user == config["user"] and password == config["password"] """


@post("/set/<id>")
def set(id):
    noCors()

    if not os.path.exists("./files/"):
        os.mkdir("./files/")
    
    file = request.files.get("file")
    file.save("./files/"+id, overwrite=True)

    return json.dumps({"message": "成功", "state": "success"})


@route("/get/<id>")
def get(id):
    noCors()
    
    return static_file(id, root="./files/")


@route("/")
def index():
    return "<h1>项目地址: <a href='https://github.com/dffxd-suntra/xesb-memorizer'>https://github.com/dffxd-suntra/xesb-memorizer</a></h1>"


config = readConfig()
print(config)

run(host=config["host"], port=config["port"])
