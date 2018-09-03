import hashlib

from flask_restful import Resource


def md5(pas):
    md5 = hashlib.md5()
    md5.update(pas.encode('utf-8'))
    return md5.hexdigest()

# 登陆
class Login(Resource):
    pass



#注册
class Regist(Resource):
    pass



# 购物车
class Shopcar(Resource):
    pass


# 订单
class Orede(Resource):
    pass



# 主页面
class Main(Resource):
    pass
