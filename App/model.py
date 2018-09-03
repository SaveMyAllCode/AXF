
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_sql(app):
    db.init_app(app=app)

class axf_foodtypes(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    typeid = db.Column(db.String(200))
    typename = db.Column(db.String(200))
    childtypenames = db.Column(db.String(200))
    typesort = db.Column(db.Integer,default=0)

    def axf_foodtypes_dict(self):
        return {'id':self.id,'typeid':self.typeid,'typename':self.typename,'childtypenames':self.childtypenames,'typesort':self.typesort}


class axf_goods(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    productid = db.Column(db.String(20))
    productimg = db.Column(db.String(200))
    productname = db.Column(db.String(200))
    productlongname = db.Column(db.String(200))
    isxf = db.Column(db.Integer,default=0)
    pmdesc = db.Column(db.Integer,default=0)
    specifics = db.Column(db.String(20))
    price = db.Column(db.Float,default=0)
    marketprice = db.Column(db.Float,default=0)
    categoryid = db.Column(db.Integer)
    childcid = db.Column(db.Integer)
    childcidname = db.Column(db.String(100))
    dealerid = db.Column(db.String(10))
    storenums = db.Column(db.Integer)
    productnum = db.Column(db.Integer)
    def axf_foods_dict(self):
        return {'id':self.id,'productid':self.productid,'productimg':self.productimg,'productname':self.productname,
                'productlongname':self.productlongname,'isxf':self.isxf,'pmdesc':self.pmdesc,'specifics':self.specifics,
                'price':self.price,'marketprice':self.marketprice,'categoryid':self.categoryid,'childcid':self.childcid,
                'childcidname':self.childcidname,'dealerid':self.dealerid,'storenums':self.storenums,'productnum':self.productnum}