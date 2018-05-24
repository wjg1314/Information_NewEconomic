
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
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
    # from flask import session
    #会将{‘age’:'18'},写入到cookie
    # session["age"] = '18'
    return "index"

if __name__ == '__main__':
    manager.run()