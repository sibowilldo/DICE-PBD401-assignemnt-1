"""create vacancies table

Revision ID: 4c04d76d2276
Revises: bd40321fa721
Create Date: 2023-03-13 00:07:37.826288

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47bd3fb2a311'
down_revision = '4c04d76d2276'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'vacancies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('category_id', sa.Integer),
        sa.Column('type_id', sa.Integer),

        sa.Column('title', sa.String),
        sa.Column('description', sa.Text),
        sa.Column('department', sa.Text),
        sa.Column('location', sa.Text),
        sa.Column('expires_at', sa.DateTime()),

        sa.Column('created_at', sa.DateTime(), default=datetime.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=True),

        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], None, 'CASCADE', 'CASCADE'),
        sa.ForeignKeyConstraint(['category_id'], ['categories.id'], None, 'CASCADE', 'CASCADE'),
        sa.ForeignKeyConstraint(['type_id'], ['types.id'], None, 'CASCADE', 'CASCADE'),
    )


def downgrade():
    op.drop_table('vacancies')
