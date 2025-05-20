from flask import Blueprint, render_template

views = Blueprint('views', __name__) #define file as a blueprint file

@views.route('/')
def home():
    return render_template("home.html")
    #return "<p>Home<p>"

@views.route('/project_1')
def project_1():
    return render_template("project_1.html")
    #return "<p>Home<p>"

@views.route('/project_2')
def project_2():
    return render_template("project_2.html")
    #return "<p>Home<p>"

@views.route('/project_3')
def project_3():
    return render_template("project_3.html")
    #return "<p>Home<p>"

@views.route('/project_4')
def project_4():
    return render_template("project_4.html")
    #return "<p>Home<p>"