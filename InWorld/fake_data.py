'''
构造虚拟数据
'''


import random
from faker import Faker
from sqlalchemy.exc import IntegrityError

from InWorld.models import db, User, Post


fake = Faker(locals='zh_CN')

def faker_user():
    user = User(
        username = 'weber',
        power = 1,
        password = '111111'
    )
    db.session.add(user)
    db.session.commit()

def faker_post(count=10):
    for i in range(count):
        post = Post(
            title = fake.sentence(),
            body = fake.text(300),
            publish_date = fake.past_datetime()
        )
        db.session.add(post)
    db.session.commit()

def create_fake_data():
    #    随机生成例子文章的脚本
    import random
    import datetime
    from faker import Faker

    myfaker = Faker(locale="zh_CN")
    try:
        user = User.query.get(1)
    except Exception as ex:
        print(ex)
        user = User(username='faker_name')
        db.session.add(user)
        db.session.commit()
    tag_one = Tag('人生')
    tag_two = Tag('苦痛')
    tag_three = Tag('热泪')
    tag_four = Tag('盈眶')
    tag_list = [tag_one, tag_two, tag_three, tag_four]

    for i in range(10):
        new_post = Post(myfaker.sentence())
        new_post.user = user    
        new_post.publish_date=datetime.datetime.now()  
        new_post.text = myfaker.text(300)
        new_post.tags = random.sample(tag_list, random.randint(0,3))    
        db.session.add(new_post)
    db.session.commit()