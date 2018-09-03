from flask_restful import Api

from App.apis import Login, Regist, Shopcar
from App.model import Base

api = Api()

api.add_resource(Login,'/login/')
api.add_resource(Regist,'/regist/')
api.add_resource(Shopcar,'/shopcar/')



def init_api(app):
    api.init_app(app=app)