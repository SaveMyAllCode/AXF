from flask_restful import Api

from App.apis import Login, Regist, Shopcar, Order, Main, Market

api = Api()

api.add_resource(Login, '/login/')
api.add_resource(Regist, '/regist/')
api.add_resource(Shopcar, '/shopcar/')
api.add_resource(Order, '/order/')
api.add_resource(Main, '/main/')
api.add_resource(Market, '/market/')


def init_api(app):
    api.init_app(app=app)
