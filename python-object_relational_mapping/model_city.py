#!/usr/bin/python3
"""
Module that defines the State class linked to the MySQL table 'cities'
using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    cities class that inherits from Base and links to the 'cities' table.
    """
    __tablename__ = 'cities'

    # عمود المعرف (id): رقم فريد، أساسي، لا يمكن أن يكون فارغاً، ويولد تلقائياً
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # عمود الاسم (name): نص بطول أقصى 128 حرفاً، ولا يمكن أن يكون فارغاً
    name = Column(String(128), nullable=False)
    # عمود state_id: مفتاح أجنبي يربط المدينة بجدول states
    state_id = Column(Integer, ForeignKey('states.id') nullable=False)
