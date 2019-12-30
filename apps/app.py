from flask import Flask, render_template    # Render Template via Flask
from flask_pymongo import PyMongo           # Use PyMongo to interact with Mongo DB
import scraping                             # Use scraping code

app = Flask(__name__)
# App will connect to Mongo using URI & the URI used to connect to mongo via port 27017
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"      
mongo = PyMongo(app) 

@app.route("/") # Tells flask what to display when looking at home page
def index():
    mars = mongo.db.mars.find_one()     # Find the mars collection in DB
    return render_template("index.html", mars=mars) #return an HTML file & use mars collection

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scrape_mars.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"

if __name__ == "__main__":
   app.run()