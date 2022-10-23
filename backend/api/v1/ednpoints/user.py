"""
 @Author: Jason
 @Email: zzengyun@126.com
 @FileName: login.py
 @DateTime: 2022/10/23 17:51
 @SoftWare: PyCharm
"""
from typing import List

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from backend.models import User
from backend.scheams import User_pydantic, UserIn_pydantic
from backend.core import verify_password, create_access_token
from fastapi.requests import Request

user = APIRouter(tags=["认证相关"])


@user.post("/login", summary="登录")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    if userinfo := await User.get(username=form_data.username):
        if verify_password(form_data.password, userinfo.password):
            return {"access_token": create_access_token({"id": userinfo.username}), "token_type": "bearer"}
    return {"msg": "账号或密码错误"}


@user.post("/user_add", summary="新增用户")
async def user_add(user_form: UserIn_pydantic):
    # if await User.filter(username = user.username)
    if await UserIn_pydantic.from_tortoise_orm(await User.create(**user_form.dict())):
        return {"msg":"账号新增成功！","code":200}
    else:
        return {"msg": "账号新增失败！", "code": 400}


@user.post("/user_update/{username}", summary="修改用户信息")
async def user_update(username: str, user_form: UserIn_pydantic):
    if await User.filter(username=username).update(**user_form.dict()):
        return {"msg": "update"}
    return {"msg": "error"}


@user.post("/user_list", summary="用户列表", response_model=List[User_pydantic])
async def user_list(limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    return await User_pydantic.from_queryset(User.all().offset(skip).limit(limit))
