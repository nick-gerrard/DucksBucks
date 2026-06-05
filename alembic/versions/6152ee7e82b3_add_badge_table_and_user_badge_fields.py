"""add badge table and user badge fields

Revision ID: 6152ee7e82b3
Revises: c86aa1e91a06
Create Date: 2026-06-05 18:33:20.024654

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6152ee7e82b3'
down_revision: Union[str, Sequence[str], None] = 'c86aa1e91a06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('user', sa.Column('badge', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('favorite_team', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('badge_expiration', sa.Date(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('user', 'badge_expiration')
    op.drop_column('user', 'favorite_team')
    op.drop_column('user', 'badge')
