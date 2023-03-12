"""create types table

Revision ID: 93cb8569643f
Revises: 7d1df5103632
Create Date: 2023-03-12 23:13:02.790190

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa

from models.type import table_name

# revision identifiers, used by Alembic.
revision = '93cb8569643f'
down_revision = '7d1df5103632'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        table_name,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('created_at', sa.DateTime(), default=datetime.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table(table_name)
