#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa using SQLAlchemy.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    # إنشاء محرك الاتصال SQLAlchemy
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    #إنشاء الجلسة (Session)
    Session = sessionmaker(bind=engine)
    session = Session()

    # جلب جميع الولايات التي تحتوي على حرف 'a'
    states = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    # حذف كل ولاية تم العثور عليها
    for state in states:
        session.delete(state)

    # حفظ التغييرات واعتماد الحذف في قاعدة البيانات
    session.commit()

    # إغلاق الجلسة
    session.close()
