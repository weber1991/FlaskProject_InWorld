from flask import Flask, redirect, url_for
from InWorld.models import db
from InWorld.controllers.api.blog import PostList
from InWorld.controllers.blog import blog_blueprint
from flask_restful import Api



# 使用工厂模式
def create_app(object_name):
    # 实例一个flask项目
    app = Flask(__name__)

    # 调用选择的模式
    # 在config.py文件里面：webapp.config.DecConfig / webapp.config.ProConfig
    app.config.from_object(object_name)
    
    # 将数据库注册到实例
    db.init_app(app)

    # api模块注册到实例
    api = Api(app)
    api.add_resource(PostList, '/api/blog/postlist')

    # 蓝本注册
    app.register_blueprint(blog_blueprint, url_prefix = '/blog')
    return app