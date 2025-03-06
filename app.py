from flask import Flask
from flask import render_template
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/base')
def base_page():
    return render_template('base.html')

@app.route('/about')
def about_page():
    return render_template('about.html')
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to ACME Labs Inc!"

if __name__ == '__main__':
    app.run(debug=True)