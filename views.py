from main import app
from flask import render_template

#rotas
@app.route('/')
def homePage():
    return render_template('home.html')