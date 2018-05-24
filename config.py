from redis import StrictRedis



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