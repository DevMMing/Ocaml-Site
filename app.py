#Ocaml Presentation -- Matthew Ming
from flask import Flask, render_template, redirect, url_for, session, request, flash, get_flashed_messages

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
