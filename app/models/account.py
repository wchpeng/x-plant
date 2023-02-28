from tortoise import fields, Model


class User(Model):
    """用户信息"""
    username = fields.CharField(128, default='', description='用户名')
    avatar = fields.CharField(256, default='', description='用户头像')
    password = fields.CharField(256, default='', description='密码')
    mobile = fields.CharField(16, default='', description='电话号')
    role = fields.IntField(default=0, description='角色：admin, user')
    is_disable = fields.BooleanField(default=False, description='是否禁用')

    update_time = fields.DatetimeField(auto_now=True, description='修改时间')
    create_time = fields.DatetimeField(auto_now_add=True, description='创建时间')

    class Meta:
        table = 'users'
