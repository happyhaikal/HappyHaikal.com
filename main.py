from website import create_app 
from flask import Flask, render_template

#website is a python package as has init.py inside it

app = create_app()

#run flask server, only run webserver if run this file directly
if __name__ == '__main__':
    app.run(debug=True) #debug = True which means if got change to pyton code, will auto rerun webserver
