#coding utf-8
import os
import importlib


def fuck(webfinger,url):

    for exp in os.listdir("./plugin"):
        exp = exp.strip()
        if exp.split(".")[1] == "py" and exp.split(".")[0] != '__init__':
            r = importlib.import_module('plugin.' + exp.split(".")[0])
            
            if r.assign(webfinger,url):
                r.audit(url)
                
fuck("dedecms","http://157.119.232.158/")
