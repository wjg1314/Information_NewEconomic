from info import app,db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand



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