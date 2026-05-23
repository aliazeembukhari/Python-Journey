from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask! Your ML API is alive'

app.route('/about')
def about():
    return 'This is a simple route example to About page'

app.route('/contact')
def contact():
    return "<h2>Contact us<h2><p>Email: aliazeembukhari93@gmail.com<p>"

if __name__== "__main__":
    app.run(debug=True, use_reloader=False)