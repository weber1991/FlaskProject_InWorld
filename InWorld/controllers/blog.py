from InWorld.models import db, User, Tag, Post
from flask import Blueprint,render_template
from os import path




'''
创建蓝图->注册蓝图->通过ajax来获取接口资源->vue来渲染页面
'''

blog_blueprint = Blueprint(
    'blog',
    __name__,
    template_folder='../templates/blog',
)

@blog_blueprint.route('/')
def index():
    return render_template('index.html')


@blog_blueprint.route('/post/<int:post_id>', method=['GET'])
def show_post(post_id):
    pass