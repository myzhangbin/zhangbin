# coding: UTF-8 
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from app import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():

	return render_template("main2.html")


@app.route('/Info')
def info():

	return "公司信息，未完成"
	return render_template("main2.html")


@app.route('/Examples')
def examples():

	return "案例欣赏"
	return render_template("main2.html")


@app.route('/Contact')
def contact():

	return "联系方式，未完成"
	return render_template("main2.html")