from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products():
    return "<h2>Coming Soon - Maatikala Collection</h2>"

@app.route("/about")
def about():
    return "<h2>Maatikala - Crafted from Earth</h2>"

# This line is required for Vercel
app = app