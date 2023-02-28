from typing import List
from datetime import datetime
from pydantic import BaseModel, Field, validator


class RhizomeListItemSchema(BaseModel):
    """作品详情"""
    id: str = Field(..., description='ID')
    name: str = Field(..., description='名字')
    desc: str = Field(..., description='描述')
    model1: list = Field(..., description='模型1')
    model2: list = Field(..., description='模型2')
    model3: list = Field(..., description='模型3')
    model4: list = Field(..., description='模型4')
    create_time: datetime = Field(..., description='创建时间')


class RhizomeListSchema(BaseModel):
    total: int
    list: List[RhizomeListItemSchema]
