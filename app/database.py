"""پایگاه داده و تنظیمات SQLAlchemy"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# مسیر پایگاه داده SQLite
DATABASE_URL = "sqlite:///./toolora.db"

# ایجاد Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # برای SQLite
)

# ایجاد SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base برای مدل‌ها
Base = declarative_base()

def get_db():
    """Dependency برای دریافت Session در API"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """ایجاد تمام جداول"""
    Base.metadata.create_all(bind=engine)
