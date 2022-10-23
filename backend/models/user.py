"""
 @Author: Jason
 @Email: zzengyun@126.com
 @FileName: user.py
 @DateTime: 2022/10/23 17:52
 @SoftWare: PyCharm
"""
from typing import Iterable, Optional

from tortoise import models, BaseDBAsyncClient
from tortoise import fields

from backend.core import get_password_hash


class User(models.Model):
    username = fields.CharField(max_length=20, null=False, description="账号")
    password = fields.CharField(max_length=128, null=False, description="密码")
    email = fields.CharField(max_length=128, null=True, description="邮箱")
    profession = fields.CharField(max_length=1,default=1, description="职位,1(测试工程师)，2（产品经理），3（后端开发），4（前端开发）")
    feishu_id = fields.CharField(max_length=100, null=True, description="飞书id")

    async def save(
        self,
        using_db: Optional[BaseDBAsyncClient] = None,
        update_fields: Optional[Iterable[str]] = None,
        force_create: bool = False,
        force_update: bool = False,
    ) -> None:
        if force_create or "password" in update_fields:
            self.password = get_password_hash(self.password)
        await super(User, self).save(using_db, update_fields, force_create, force_update)