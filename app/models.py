"""مدل‌های پایگاه داده"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from app.database import Base

class ToolUsage(Base):
    """مدل برای ثبت استفاده از ابزارها"""
    __tablename__ = "tool_usage"
    
    id = Column(Integer, primary_key=True, index=True)
    tool_name = Column(String(50), index=True)  # نام ابزار
    input_data = Column(Text)  # داده ورودی
    output_data = Column(Text)  # داده خروجی
    timestamp = Column(DateTime, default=datetime.utcnow)  # زمان استفاده
    
    def __repr__(self):
        return f"<ToolUsage(tool={self.tool_name}, timestamp={self.timestamp})>"
