from flask import Flask, render_template

app = Flask(__name__,
            template_folder="templates",
            static_folder="static/static")

# Sample product list (later can connect to database)
products_data = [
    {
        "name": "Terracotta Pot",
        "price": "₹799",
        "image": "images/front-view-dolma-along-with-yogurt-inside-brown-pots-grey-floor.jpg"
    },
    {
        "name": "Clay Diya Set",
        "price": "₹299",
        "image": "images/front-view-dolma-along-with-yogurt-inside-brown-pots-grey-floor.jpg"
    },
    {
        "name": "Mud Table Lamp",
        "price": "₹1,499",
        "image": "images/front-view-dolma-along-with-yogurt-inside-brown-pots-grey-floor.jpg"
    }
]

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