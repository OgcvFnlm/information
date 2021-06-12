from flask import Flask
from flask_session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis

from config import Config
db = SQLAlchemy()
redis_store = None


def create_app(config_name):
    """通过传入不同的配置名字，初始化其对应配置的应用实例"""
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    global redis_store
    redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

    CSRFProtect(app)

    Session(app)

    from info.modules.index import index_blu
    app.register_blueprint(index_blu)

    return app

