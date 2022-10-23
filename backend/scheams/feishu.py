"""
 @Author: Jason
 @Email: zzengyun@126.com
 @FileName: feishu.py
 @DateTime: 2022/10/23 19:03
 @SoftWare: PyCharm
"""
from tortoise.contrib.pydantic import pydantic_model_creator
from backend.models import Feishu

Feishu_pydantic = pydantic_model_creator(Feishu, name="Feishu")
FeishuIn_pydantic = pydantic_model_creator(Feishu, name="FeishuIn")