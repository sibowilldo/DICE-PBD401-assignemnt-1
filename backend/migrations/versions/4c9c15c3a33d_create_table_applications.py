"""create table applications

Revision ID: 4c9c15c3a33d
Revises: 47bd3fb2a311
Create Date: 2023-03-13 00:50:01.728713

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4c9c15c3a33d'
down_revision = '47bd3fb2a311'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'applications',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('status_id', sa.Integer),
        sa.Column('vacancy_id', sa.Integer),

        sa.Column('created_at', sa.DateTime(), default=datetime.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=True),

        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], None, 'CASCADE', 'CASCADE'),
        sa.ForeignKeyConstraint(['status_id'], ['statuses.id'], None, 'CASCADE', 'CASCADE'),
        sa.ForeignKeyConstraint(['vacancy_id'], ['vacancies.id'], None, 'CASCADE', 'CASCADE'),
    )


def downgrade():
    op.drop_table('applications')
