"""Renaming students to scholars

Revision ID: d499975c134d
Revises: 
Create Date: 2025-05-25 18:29:45.196660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd499975c134d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # op.rename_table('students', 'scholars')

    pass


def downgrade() -> None:

    # op.rename_table('scholars', 'students')
    pass
