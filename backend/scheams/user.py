"""
 @Author: Jason
 @Email: zzengyun@126.com
 @FileName: user.py
 @DateTime: 2022/10/23 17:52
 @SoftWare: PyCharm
"""
from tortoise.contrib.pydantic import pydantic_model_creator
from backend.models import User

User_pydantic = pydantic_model_creator(User, name="User", exclude=['password'])
UserIn_pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)