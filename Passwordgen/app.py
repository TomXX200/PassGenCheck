from flask import Flask, render_template, request, redirect, url_for, session
import random
import string
import re

app = Flask(__name__)
app.secret_key = 'tfghq'

def password_check(password):
    score = 0
    
    if len (password) >=8:
        score+=1
    
    if re.search(r'[A-Z]', password):
        score+=1

    if re.search(r'\d', password):
        score+=1

    if re.search(r'[!@^"£*]', password):
        score+=1
    if score <1:
        return 'Weak'
    elif score <4:
        return 'Ok'
    else:
        return 'Strong'

symbolrandom = ['!', '@', '^', '"', '£', '*']

@app.route('/')
def home():
    generated = session.pop('generated', None)
    return render_template('index.html', generated=generated)

@app.route('/generate', methods=['POST'])
def generate():
    password_length = 12
    first = request.form['first']
    surname = request.form['surname']
    date = request.form['date']
    symbol = request.form.get('symbol', '')
    random_symbols = random.choice(symbolrandom)

    if symbol == 'on':
        combined = first + surname + date + random_symbols
    else:
        combined = first + surname + date

    session['generated'] = combined
    
    return render_template('index.html', generated=combined)

@app.route('/test', methods=['POST'])
def test():
    password = request.form.get('password')
    test = password_check(password)
    return render_template('index.html', tested=test)

if __name__ == "__main__":
    app.run(debug=True)

