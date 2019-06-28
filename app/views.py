from flask import render_template

from app import app, models

import db

@app.route('/')
def main_page():

  products = db.session.query(models.Product).\
    all()
  
  return render_template('index.html', products=[p.to_json() for p in products])

@app.route('/cart')
def cart_page():

  products = db.session.query(models.Product).\
    all()
  
  return render_template('cart.html', products=[p.to_json() for p in products])