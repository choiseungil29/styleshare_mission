import json

# TODO: buy api 만들기
# stock 줄여주는 코드 추가
# 클라이언트 localStorage 초기화하는 문제는 어떻게 해결할 것인가?
# 클라이언트의 모든 페이지에서 products를 가져가고, product_id로 find하는 함수 작성

from functools import reduce

from flask import request

from app import app, models

import db


@app.route('/api/buy', methods=['POST'])
def buy():
  """
  buy api
  request POST
    cart: [] (order info list)
  """
  products = json.loads(request.data)

  product_price = 0
  shipping_price = 0
  total_price = 0

  providers = {}
  for data in products:
    product = db.session.query(models.Product).\
      filter(models.Product.id == data['product']['id']).\
      one()

    option = list(filter(lambda x: x.id == data['option']['id'], product.options))[0]
    option.stock -= data['count']

    product_price += data['count'] * product.price

    if product.provider not in providers:
      providers[product.provider] = []
    providers[product.provider].append(product)
  
  for products in providers.values():
    bundles = filter(lambda x: x.can_bundle, products)
    # not_bundles = set(products) - set(bundles)
    not_bundles = filter(lambda x: not x.can_bundle, products)

    bundles = list(map(lambda x: x.shipping_price, bundles))
    if len(bundles) <= 0:
      bundles = [0]
    price = min(bundles)
    shipping_price += price

    shipping_price += reduce(lambda x, y: x + y.shipping_price, not_bundles, 0)   
  
  total_price = product_price + shipping_price

  res = {
    'product_price': product_price,
    'shipping_price': shipping_price,
    'total_price': total_price
  }

  db.session.commit()
  return json.dumps(res)
  