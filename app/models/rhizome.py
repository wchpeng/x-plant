"""购物车"""
from tortoise import fields, Model


class Rhizome(Model):
    """作品"""
    userid = fields.IntField(default=0, description='用户ID')
    name = fields.CharField(128, default='', description='名称')
    desc = fields.CharField(128, default='', description='描述')
    model1 = fields.JSONField(default='[]', description='整体模型')
    model2 = fields.JSONField(default='[]', description='单根模型')
    model3 = fields.JSONField(default='[]', description='实体模型')
    model4 = fields.JSONField(default='[]', description='仪器模型')
    is_deleted = fields.BooleanField(default=False, description='是否删除')
    update_time = fields.DatetimeField(auto_now=True, description='修改时间')
    create_time = fields.DatetimeField(auto_now_add=True, description='创建时间')

    class Meta:
        table = 'rhizomes'
