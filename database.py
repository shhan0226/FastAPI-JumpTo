# import contextlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"
# MariaDB 연결 문자열 (사용자명, 비밀번호, 호스트, 포트, 데이터베이스 이름을 설정하세요)

db = {
    'user': 'vraptor',
    'password': 'vraptor',
    'host': '192.168.0.5',
    'port': 3306,
    'database': 'myapi'
}

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"


engine = create_engine(
   SQLALCHEMY_DATABASE_URL
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# @contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
