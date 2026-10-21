#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
where id = 2 to "New Mexico" using SQLAlchemy.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # إنشاء محرك الاتصال SQLAlchemy
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # إنشاء الجلسة (Session)
    Session = sessionmaker(bind=engine)
    session = Session()

    # جلب الولاية المطابقة للاسم عبر المعامل الرابع باستخدام .first()
    state = session.query(State).filter(State.id == 2).first()

    # طباعة  id إذا وُجدت، أو Not found إذا لم تكن موجودة
    if state is not None:
        state.name = "New Mexico"
        session.commit()

    # إغلاق الجلسة
    session.close()
