#!/usr/bin/python3
"""
Module that defines the State class linked to the MySQL table 'states'
using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# إنشاء الكائن الأساسي للـ ORM
Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base and links to the 'states' table.
    """
    __tablename__ = 'states'

    # عمود المعرف (id): رقم فريد، أساسي، لا يمكن أن يكون فارغاً، ويولد تلقائياً
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # عمود الاسم (name): نص بطول أقصى 128 حرفاً، ولا يمكن أن يكون فارغاً
    name = Column(String(128), nullable=False)
