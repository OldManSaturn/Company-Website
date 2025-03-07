from flask import Flask, render_template, request

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
@app.route('/legal')
def legal_page():
    return render_template('legal.html')
@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        # Handle form submission
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Process the form data (e.g., save to database, send email, etc.)
        return render_template('contact.html', success=True)
    return render_template('contact.html')

@app.route('/base')
def base_page():
    return render_template('base.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)