from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/products')
def products_page():
    return render_template('products.html')
@app.route('/partnerships')
def partnerships_page():
    return render_template('partnerships.html')
@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/base')
def base_page():
    return render_template('base.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)