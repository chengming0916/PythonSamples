#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models import Base, Engine
import models


if __name__ == "__main__":
    # 删除表
    Base.metadata.drop_all(Engine)

    # 创建表
    Base.metadata.create_all(Engine)

    user = models.UserInfo(
        username="张三", phone="12345678910", address="TJ", gender="male"
    )

    models.session.add(user)

    # 提交
    models.session.commit()

    # 本次修改具有字符串字段在原值基础上做更改的操作，所以必须添加 synchronize_session=False
    models.session.query(models.UserInfo).filter_by(username="张三").update(
        {"username": "李四"}, synchronize_session=False
    )

    # 关闭连接， 或使用 session.remove() 回收连接
    models.session.close()
