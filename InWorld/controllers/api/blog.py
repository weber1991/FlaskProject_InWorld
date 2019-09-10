from flask_restful import Resource
from flask_restful import fields, marshal_with, marshal
from InWorld.models import db, User, Tag, Post
from InWorld.fake_data import create_fake_data


# 构造序列化数据的类
class PostListFields:
    '''
    构造序列格式类，利用的是fields
    从小到大构造，从内到外构造
    '''
    # 构造标签序列
    taglist={
        'id':fields.Integer(),
        'title':fields.String()
    }
    postlist={
        'title':fields.String(attribute = 'title'),
        'text':fields.String(attribute='text')  # 需要设置成过滤html模式

    }
    resource = {
        'success':fields.Boolean(attribute='success'),
        'postlist':fields.List(fields.Nested(postlist))
    }

class PostListWrapper:
    '''
    包装数据类：将数据序列化的函数
    '''
    @staticmethod
    def _res_stuct(error, postlist):
        return dict(success=error, postlist=postlist)
    
    @staticmethod
    def wrapper(error, postlist=[]):
        wrapper_postlist = []
        # 构造文章序列
        for post in postlist:
            # 遍历文章，将每个文章改进
            wrapper_postlist.append(marshal(
                {'title':post.title, 'text':post.text}, PostListFields.postlist
                ))
        value = dict(success=error,postlist=wrapper_postlist)
        wrapper_resource = marshal(value, PostListFields.resource)
        return wrapper_resource

class PostList(Resource):
    def get(self, page=1):
        # 生成虚假数据的脚本
        # create_fake_data()
        try:
            # postList = Post.query.order_by(
            #     Post.publish_date.desc()
            # ).paginate(page, 10)
            postList = Post.query.all()
            ans = PostListWrapper.wrapper(True, postList)
            return ans
        except Exception as ex:
            print(ex)
            return PostListWrapper.wrapper(False, '')
