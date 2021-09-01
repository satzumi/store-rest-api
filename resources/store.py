from flask_restful import Resource,reqparse
from models.store import StoreModel


class Store(Resource):
    
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {'message': 'no store with this name'},404
            
    def post(self,name):
        
        store = StoreModel.find_by_name(name)
        if store:
            return {'message':'already exists'}
        
    
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'internal error occured'},500
        return store.json()
        
    def delete(self):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        
        return {'message':'store is deleted'}
        
class StoreList(Resource):
    def get(self):
        return {'stores': [ store.json() for store in  StoreModel.query.all()]}
        