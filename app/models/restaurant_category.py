from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base
from sqlalchemy.orm import relationship


class RestaurantCategory(Base):  # Added colon
    __tablename__ = "restaurant_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)

    # Establish a bidirectional relationship between Restaurant and RestaurantCategory tables
    # so that the 'category' field is defined in the restaurant table
    restaurants = relationship("Restaurant", back_populates="category")