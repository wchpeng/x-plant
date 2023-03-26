from typing import List
from datetime import datetime
from pydantic import BaseModel, Field, validator


class RhizomeModelSchema(BaseModel):
    image: str = Field(..., description='图片')


class RhizomeListItemSchema(BaseModel):
    """作品详情"""
    id: str = Field(..., description='ID')
    name: str = Field(..., description='名字')
    desc: str = Field(..., description='描述')
    model1: list = Field(List[RhizomeModelSchema], description='模型1,整体模型')
    model2: list = Field(List[RhizomeModelSchema], description='模型2,单根模型')
    model3: list = Field(List[RhizomeModelSchema], description='模型3,实体模型')
    model4: list = Field(List[RhizomeModelSchema], description='模型4,仪器模型')
    create_time: datetime = Field(..., description='创建时间')


class RhizomeListSchema(BaseModel):
    total: int
    list: List[RhizomeListItemSchema]
