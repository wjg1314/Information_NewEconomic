from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
# from config import Config,DevlopmentConfig,ProductionConfig,UnittestConfig
from config import configs

#创建连接到sqlchemy数据库的对象
db = SQLAlchemy() 

def create_app(config_name):

    # 创建app的工厂方法
    # 参数：根据参数选择不同的配置类


    app = Flask(__name__)

    #获取配置信息
    app.config.from_object(configs[config_name])

    #创建连接到MYSQL数据库的对象
    # db = SQLAlchemy(app)
    db.init_app(app)

    #创建连接到redis数据库的对象
    redis_store = StrictRedis(host=configs[config_name].REDIS_HOST,port=configs[config_name].REDIS_PORT)

    #开启csrf保护：因为项目中的表单不再使用flaskform来实现，#指定session数据存储在后端的位置所以不会自动开启csrf保护，需要自己开启
    CSRFProtect(app)

    #指定session数据存储在后端的位置
    Session(app)

    return app