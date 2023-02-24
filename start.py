from bottle import route, run, static_file, request, response, abort
import json
import re
import os


def readConfig():
    file = open("config.json", encoding="utf-8")
    return json.loads(file.read())


""" def checkUser(user, password):
    return user == config["user"] and password == config["password"] """


@route("/set/<id>/")
def set(id):
    (not os.path.exists("./files/")) and os.mkdir("./files/")

    file = open("./files/"+id, "w+", encoding="utf-8")
    file.write(request.files.get('file'))
    file.close()

    print(request.files.get('file'))
    
    return json.dumps({"message": "成功", "state": "success"})


@route("/get/<id>/")
def get(id):
    return static_file(id, root="./files/")


@route("/")
def index():
    return "<h1>项目地址: <a href='https://github.com/dffxd-suntra/xesb-memorizer'>https://github.com/dffxd-suntra/xesb-memorizer</a></h1>"


config = readConfig()
print(config)

run(host=config["host"], port=config["port"])
