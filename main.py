from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user (replace later with database validation)
USER_CREDENTIALS = {"username": "admin", "password": "1234"}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
        # If login is correct, go to index.html
        return redirect(url_for('index'))
    else:
        return "Invalid username or password. Try again!"

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
