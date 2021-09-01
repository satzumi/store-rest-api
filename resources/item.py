from flask import Flask,request
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):   
    def get(self,name):
        
        item =  ItemModel.find_by_name(name)
        if item:
            return item.json()
        else:
            return {'message':'Item not found'}, 404

    
    def post(self,name):
   
        if ItemModel.find_by_name(name):
            return { 'message' : "An item with name {} already exists".format(name)}

        parser = reqparse.RequestParser()
        parser.add_argument(
            'price',
            type=float,
            required=True,
            help='This field cannot be left blank'
        )
        parser.add_argument(
            'store_id',
            type=int,
            required=True,
            help='Every item has a store_id'
        )        
        
        data = parser.parse_args()
        item = ItemModel(name,data['price'],data['store_id'])
        item.save_to_db()
        return item.json(), 201              #item is created
    
    def put(self,name):
        
        parser = reqparse.RequestParser()
        parser.add_argument(
            'price',
            type=float,
            required=True,
            help='This field cannot be left blank'
        )
        parser.add_argument(
            'store_id',
            type=int,
            required=True,
            help='Every item has a store_id'
        )        
        
        data = parser.parse_args()
        
        item = ItemModel.find_by_name(name)
        
        if item is None:
            item = ItemModel(name,data['price'],data['store_id'])
        else:
            item.price = data['price']
            
        item.save_to_db()
        return item.json()
        
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_model()
        return {'message':'item deleted'}
    
class Items(Resource):
    def get(self):
        return {"items":[item.json() for item in ItemModel.query.all() ]}