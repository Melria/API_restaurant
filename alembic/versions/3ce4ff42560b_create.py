"""create

Revision ID: 3ce4ff42560b
Revises: 
Create Date: 2025-11-03 14:57:47.355706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ce4ff42560b'
down_revision: str = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    pass

def downgrade() -> None:
    pass