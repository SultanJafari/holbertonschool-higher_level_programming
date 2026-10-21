#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
using SQLAlchemy.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # إنشاء محرك الاتصال  SQLAlchemy
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    #  إنشاء الجلسة (Session)
    Session = sessionmaker(bind=engine)
    session = Session()

    #  جلب جميع كائنات الولايات مرتبة تصاعدياً حسب  id
    states = session.query(City, State).join(Stat, City.state_id == State.id).order_by(City.id.asc()).all
    # طباعة النتائج بصيغة (id: name)
    for city, state in results:
        print("{}: {}".format(state.name, city.id, city.name))

    # إغلاق الجلسة
    session.close()
