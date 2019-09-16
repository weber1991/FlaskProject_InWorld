from InWorld.models import db, User, Tag, Post, tags
from flask import Blueprint,render_template
from os import path
from sqlalchemy import func




def sidebar_data():
    '''
    '''
    recent = Post.query.order_by(
        Post.publish_date.desc()
    ).limit(5).all()
    top_tags = db.session.query(
        Tag, func.count(tags.c.post_id).label('total')
    ).join(
        tags
    ).group_by(Tag).order_by().limit(5).all()
    return recent, top_tags

'''
1)创建蓝图->注册蓝图->通
2)改进用api，然后ajax来获取接口资源->vue来渲染页面
'''
blog_blueprint = Blueprint(
    'blog',
    __name__,
    template_folder='../templates/blog',
)

@blog_blueprint.route('/')
@blog_blueprint.route('/<int:page>')
def index(page = 1):
    # 使用模型里面自带的分页器
    posts = Post.query.order_by(
        Post.publish_date.desc()
    ).paginate(page, 10)
    recent,  top_tags = sidebar_data()
    return render_template('index.html', posts = posts, recent = recent, top_tags = top_tags)


@blog_blueprint.route('/post/<int:post_id>', method=['GET'])
def show_post(post_id):
    pass



@blog_blueprint.errorhandler(400)
def error_400(error):
    return render_template(''), 400

@blog_blueprint.errorhandler(500)
def error_500(error):
    return render_template(''), 500