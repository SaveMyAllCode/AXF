import hashlib

from flask import jsonify, session
from flask_restful import Resource

from App.model import axf_foodtypes, axf_goods


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
class Order(Resource):
    pass



# 主页面
class Main(Resource):
    pass
# 闪购
class Market(Resource):
    def get(self):
        foodtypes = axf_foodtypes.query.all()
        typeid = session.get("typeid") or '104749'
        sort = session.get('sort') or 0
        childtypenames = session.get('childtypenames') or 0

        # 左侧导航获得所有商品的类型
        list=[]
        for i in foodtypes:
            foodty = i.axf_foodtypes_dict()
            list.append(foodty)
        # 获得目前类型的商品
        list2= []
        print('******')
        if sort == '1':
            goodslist = axf_goods.query.filter(axf_goods.categoryid == typeid).order_by('price')
        if sort == '2':
            goodslist = axf_goods.query.filter(axf_goods.categoryid == typeid).order_by('-price')
        if sort == '3':
            goodslist = axf_goods.query.filter(axf_goods.categoryid == typeid).order_by('productnum')
        else:
            goodslist = axf_goods.query.filter(axf_goods.categoryid == typeid)

        if childtypenames != 0:
            goodslist = goodslist.filter(goodslist.childcid == childtypenames)
        print(goodslist)
        for j in goodslist:
            goods = j.axf_foods_dict()
            list2.append(goods)

        # 对类别进行切割
        goodstype = axf_foodtypes.query.filter(axf_foodtypes.typeid==typeid).first()
        # ['全部分类:0', '进口水果:103534', '国产水果:103533']
        typelist = goodstype.childtypenames.split('#')
        types = []
        for str in typelist:
            types.append(str.split(':'))

        data={
            'foodtypes':list,
            'goodslist':list2,
            'typeid':typeid,
            'types':types,

        }

        return jsonify(data)

    def put(self):
        typeid = request.form.get('typeid')
        data = {
            'code':200
        }
        if not typeid:
            data['code']=400
            return jsonify(data)
        session['typeid'] = typeid
        return jsonify(data)

    def post(self):
        log = request.form.get('log')
        data = {
            'code':200
        }
        if int(log) == 1:
            goodsid = request.form.get('goodsid')
            return jsonify(data)
        if int(log) == -1:
            goodsid = request.form.get('goodsid')
            return jsonify(data)
        if int(log) == 0:
            sort = request.form.get('sort')
            session['sort'] = sort
            return jsonify(data)
        data['code'] = 400
        return jsonify(data)





