
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand




class Config(object):
    '''配置文件的加载'''

    #项目秘钥：csrf/session，还有其他的一些签名算法会用、
    SECRET_KEY = "uW6EYLDcuCyd/v0mEWDSG/QV/XVGW/WR1bfo5h1p4U32h2RAiJ0FLrZLwfqJRuwi"

    #开启调试模式
    DEBUG = True

    #配置MYSQL数据库连接信息,真实开发使用数据库真是ip
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    #不去追踪数据库的修改，节省开销
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #配置redis数据库,因为redis不是flask的扩展，只能自己读取
    REDIS_HOST ='192.168.5.129'
    REDIS_PORT = 6379

    #指定session使用什么来存储
    SESSION_TYPE = "redis"
    # 指定session数据存储在后端的位置
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    #是否使用secret_key签名你的session
    SESSION_USE_SIGNER = True
    #设置过期时间，要求SESSION_PERMANENT,True,默认是31天
    PERMANENT_SESSION_LIFETIME = 60*60*24#一天


app = Flask(__name__)

#获取配置信息
app.config.from_object(Config)

#创建连接到MYSQL数据库的对象
db = SQLAlchemy(app)

#创建连接到redis数据库的对象
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)

#开启csrf保护：因为项目中的表单不再使用flaskform来实现，#指定session数据存储在后端的位置所以不会自动开启csrf保护，需要自己开启
CSRFProtect(app)

#指定session数据存储在后端的位置
Session(app)

#创建脚本管理器对象
manager = Manager(app)
#让迁移和app和数据库建立联系
Migrate(app,db)
#将数据库迁移的脚本添加到manager
manager.add_command("mysql",MigrateCommand)


@app.route("/")
def index():
    #测试redis数据库
    # redis_store.set("name","zxc")

    #测试session
    from flask import session
    #会将{‘age’:'18'},写入到cookie
    session["age"] = '18'
    return "index"

if __name__ == '__main__':
    manager.run()