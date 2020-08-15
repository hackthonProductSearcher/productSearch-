from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from db_service import UserService, ShopService, ProductService
from playhouse.shortcuts import model_to_dict
import json
from search_function import *

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self, user_id):
        data = UserService.getById(user_id)
        return {'data': [model_to_dict(item) for item in data]}

    def put(self, user_id):
        json_data = request.get_json(force=True)
        data = UserService.update(json_data, user_id)
        return(data)

    def delete(self, user_id):
        data = UserService.delete(user_id)

class UserList(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        data = UserService.create(json_data)
        return(data)

    def get(self):
        data = UserService.getAll()
        return {'users': [model_to_dict(item) for item in data]}

class Shop(Resource):
    def get(self, shop_id):
        data = ShopService.getById(shop_id)
        return {'data': [model_to_dict(item) for item in data]}

    def put(self, user_id):
        json_data = request.get_json(force=True)
        data = ShopService.update(json_data, shop_id)
        return(data)

    def delete(self, user_id):
        data = ShopService.delete(shop_id)

class ShopList(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        data = ShopService.create(json_data)
        return(data)

    def get(self):
        data = ShopService.getAll()
        return {'shops': [model_to_dict(item) for item in data]}

class Product(Resource):
    def get(self, product_id):
        data = ProductService.getById(product_id)
        return {'data': [model_to_dict(item) for item in data]}

    def put(self, product_id):
        json_data = request.get_json(force=True)
        data = ProductService.update(json_data, product_id)
        return(data)

    def delete(self, product_id):
        data = ProductService.delete(product_id)

class ProductList(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        data = ProductService.create(json_data)
        return(data)

    def get(self):
        data = ProductService.getAll()
        return {'products': [model_to_dict(item) for item in data]}

class SearchShop(Resource):
    def get(self):
        args = request.args
        data = ShopService.find(args['q'])
        return {'shops': [model_to_dict(item) for item in data]}

class SearchProduct(Resource):
    def get(self):
        args = request.args
        data = ProductService.find(args['q'])
        return {'products': [model_to_dict(item) for item in data]}

api.add_resource(SearchShop, '/search-shop')
api.add_resource(SearchProduct, '/search-product')
api.add_resource(User, '/users/<user_id>')
api.add_resource(Product, '/products/<product_id>')
api.add_resource(Shop, '/shops/<shop_id>')
api.add_resource(UserList, '/users')
api.add_resource(ProductList, '/products')
api.add_resource(ShopList, '/shops')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='7070')

