import datetime

from sqlalchemy import Column, Integer, String, DateTime

from database import Base


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
