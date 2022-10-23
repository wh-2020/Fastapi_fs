"""
 @Author: Jason
 @Email: zzengyun@126.com
 @FileName: feishu.py
 @DateTime: 2022/10/23 18:01
 @SoftWare: PyCharm
"""
from tortoise import models
from tortoise import fields


class Feishu(models.Model):
    messages = fields.CharField(max_length=256, null=False, description="飞书消息")
    take_user = fields.CharField(max_length=50, null=False, description="接收人")
    send_time = fields.CharField(max_length=50, null=False, description="接收人")



