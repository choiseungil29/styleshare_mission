#! venv/bin/python

import os
import sys

import dotenv

import json

dotenv.load_dotenv('local.env')
sys.path.append(os.getcwd())

os.environ['POSTGRES_HOST'] = 'localhost'

import db
from app import models


with open('goods.json') as f:
  data = json.loads(f.read())

for product in data['goods']:
  options = product['options']
  shipping = product['shipping']
  del product['options']
  del product['shipping']
  p = models.Product(**product)
  p.shipping_price = shipping['price']
  p.can_bundle = shipping['canBundle']

  db.session.add(p)
  db.session.flush()
  for option in options:
    o = models.Option(**option)
    o.product_id = p.id
    db.session.add(o)
    db.session.flush()
    
db.session.commit()