"""create statuses table

Revision ID: 7d1df5103632
Revises: 
Create Date: 2023-03-12 20:32:21.371093

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '7d1df5103632'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'statuses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('model_type', sa.String(50), nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
        sa.Column('priority', sa.SmallInteger(), nullable=True, default=None),
        sa.Column('created_at', sa.DateTime(), default=datetime.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('statuses')
