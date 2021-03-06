from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.setup import Base


class Item(Base):
    """
    Table model of items
    """

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), index=True)
    description = Column(String(300), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
