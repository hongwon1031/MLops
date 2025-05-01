from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import time

# MySQL 접속 정보
DB_URL = "mysql+pymysql://testuser:testpass@db:3306/testdb"

time.sleep(5)
# DB 연결 엔진 생성
engine = create_engine(DB_URL)

# 세션 생성기
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# 모델 클래스 베이스
Base = declarative_base()

# 실제 유저 테이블 정의
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(50))
    age = Column(Integer)
    