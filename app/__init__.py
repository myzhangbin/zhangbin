
# coding: UTF-8 
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


from flask import Flask

app = Flask(__name__) 
from app import view