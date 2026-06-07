"""add_is_playoff_make_api_id_nullable

Revision ID: 44c84662714e
Revises: 6152ee7e82b3
Create Date: 2026-06-07 14:30:07.193836

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44c84662714e'
down_revision: Union[str, Sequence[str], None] = '6152ee7e82b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table('team') as batch_op:
        batch_op.add_column(sa.Column('is_playoff', sa.Boolean(), nullable=False, server_default='0'))
        batch_op.alter_column('api_id', existing_type=sa.INTEGER(), nullable=True)
        batch_op.create_unique_constraint('uq_team_abbrev', ['abbrev'])
    # All existing teams are playoff teams.
    op.execute("UPDATE team SET is_playoff = 1")


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table('team') as batch_op:
        batch_op.drop_constraint('uq_team_abbrev', type_='unique')
        batch_op.alter_column('api_id', existing_type=sa.INTEGER(), nullable=False)
        batch_op.drop_column('is_playoff')
