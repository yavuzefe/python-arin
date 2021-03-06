from flask import render_template # flask kutuphanesinden
from CLEANBLOG import app
from CLEANBLOG.forms import RegisterForm, LoginForm
 
@app.route('/')
@app.route('/home')

def index():
    return render_template('index.html', title='HOME')

@app.route('/about')
def about():
    return render_template('about.html', title='ABOUT')

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', title='REGISTER', form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='LOGIN', form = form)