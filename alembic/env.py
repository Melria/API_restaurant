import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.core.database import Base
# importer les modules modèles pour que metadata soit rempli
import app.models.restaurant
import app.models.restaurant_category

target_metadata = Base.metadata
