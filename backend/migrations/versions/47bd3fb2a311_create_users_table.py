"""create users table

Revision ID: 47bd3fb2a311
Revises: 4c04d76d2276
Create Date: 2023-03-13 00:23:18.158127

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4c04d76d2276'
down_revision = 'bd40321fa721'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.Text),
        sa.Column('created_at', sa.DateTime(), default=datetime.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('status_id', sa.Integer),

        sa.ForeignKeyConstraint(['status_id'], ['statuses.id'], None, 'CASCADE', 'CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('users')
