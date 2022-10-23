"""
 @Author: Jason
 @Email: zzengyun@126.com
 @FileName: __init__.py.py
 @DateTime: 2022/10/23 17:51
 @SoftWare: PyCharm
"""

from fastapi import APIRouter
from .ednpoints import *

v1 = APIRouter(prefix="/v1")

v1.include_router(user)
