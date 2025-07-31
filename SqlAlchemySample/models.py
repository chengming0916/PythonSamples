import datetime
from sqlalchemy import (
    DECIMAL,
    Column,
    DateTime,
    Enum,
    Index,
    Integer,
    String,
    UniqueConstraint,
    create_engine,
)
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


# 基础类
Base = sqlalchemy.orm.declarative_base()

# 创建引擎
Engine = create_engine(
    # "mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>" # MySQL-Python
    "mysql+pymysql://root:root@192.168.50.201:3306/test1?charset=utf8mb4",  # pymysql
    # "mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>", # MySQL-Connector
    # oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...] # cx_Oracle
    # 连接池大小
    pool_size=5,
    # 查看原生语句
    echo=True,
)

# 绑定引擎
Session = sessionmaker(bind=Engine)
# 创建数据库连接池，直接使用session即可为当前线程拿出一个连接对象
# 内部会采用threading.local进行隔离
session = scoped_session(Session)


class UserInfo(Base):
    """必须集成Base"""

    # 数据库中存储的表名
    __tablename__ = "user_info"
    # NOT NULL 约束
    id = Column(Integer, primary_key=True, autoincrement=True, comment="用户ID, 主键")
    username = Column(String(32), index=True, nullable=False, comment="用户名")
    phone = Column(String(11), nullable=False, unique=True, comment="手机号")
    address = Column(String(64), comment="地址")
    gender = Column(Enum("male", "female"), default="male", comment="性别")
    create_at = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    update_at = Column(DateTime, onupdate=datetime.datetime.now, comment="最后更新时间")

    # __table_args__ = (
    #     UniqueConstraint("username", "phone"),
    #     Index("address", unique=True),
    # )

    def __str__(self):
        return f"object: <id:{self.id} username:{self.username}>"
