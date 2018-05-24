from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import Config



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