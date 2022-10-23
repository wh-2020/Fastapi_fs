"""
 @Author: Jason
 @Email: zzengyun@126.com
 @FileName: __init__.py.py
 @DateTime: 2022/10/23 17:49
 @SoftWare: PyCharm
"""
import sys

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from .v1 import v1

app = FastAPI()

app.include_router(v1,prefix="/api")

import logging

fmt = logging.Formatter(
    fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.DEBUG)
sh.setFormatter(fmt)

# will print debug sql
logger_db_client = logging.getLogger("db_client")
logger_db_client.setLevel(logging.DEBUG)
logger_db_client.addHandler(sh)

logger_tortoise = logging.getLogger("tortoise")
logger_tortoise.setLevel(logging.DEBUG)
logger_tortoise.addHandler(sh)


register_tortoise(
    app,
    db_url="sqlite://:fs.sqlite:",
    modules={"models": ["backend.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)