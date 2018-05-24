from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

class Config(object):
    '''配置文件的加载'''
    #开启调试模式
    DEBUG = True

    #配置MYSQL数据库连接信息,真实开发使用数据库真是ip
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    #不去追踪数据库的修改，节省开销
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #配置redis数据库,因为redis不是flask的扩展，只能自己读取
    REDIS_HOST ='192.168.5.129'
    REDIS_PORT = 6379

app = Flask(__name__)

#获取配置信息
app.config.from_object(Config)

#创建连接到MYSQL数据库的对象
db = SQLAlchemy(app)

#创建连接到redis数据库的对象
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)

@app.route("/")
def index():
    #测试redis数据库
    redis_store.set("name","zxc")
    return "index"

if __name__ == '__main__':
    app.run(debug=True)