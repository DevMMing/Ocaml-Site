#Ocaml Presentation -- Matthew Ming

import os, csv
from flask import Flask, render_template, redirect, url_for, session, request, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route('/')
def index():
    return render_template('templates/index.html')
if __name__ == '__main__':
    app.run(debug=True)
