"""create table profiles

Revision ID: 9c9b78c3a31d
Revises: e68fcea4200f
Create Date: 2023-03-13 01:05:14.458633

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9c9b78c3a31d'
down_revision = 'e68fcea4200f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'profiles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('given_name', sa.String, nullable=True),
        sa.Column('family_name', sa.String, nullable=True),
        sa.Column('name', sa.String, nullable=True),
        sa.Column('picture', sa.String, nullable=True, default=None),
        sa.Column('created_at', sa.DateTime(), default=datetime.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=True),


        sa.ForeignKeyConstraint(['user_id'], ['users.id'], None, 'CASCADE', 'CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('profiles')
