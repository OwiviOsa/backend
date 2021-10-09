from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum, Float
from sqlalchemy.orm import relationship
from models.base import Base


class Save(Base):
    __tablename__ = 'save'
    id = Column(Integer, primary_key=True, index=True)

    created_time = Column(DateTime)
    time = Column(String)
    player_club_id = Column(Integer)
    season = Column(Integer)

    user_id = Column(Integer, ForeignKey('user.id'))
    leagues = relationship("League", backref="save", lazy='select')
    calendars = relationship("Calendar", backref="save", lazy='select')
