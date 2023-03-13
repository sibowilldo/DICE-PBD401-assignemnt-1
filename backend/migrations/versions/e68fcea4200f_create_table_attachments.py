"""create table attachments

Revision ID: e68fcea4200f
Revises: 4c9c15c3a33d
Create Date: 2023-03-13 00:53:19.673598

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e68fcea4200f'
down_revision = '4c9c15c3a33d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'attachments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('application_id', sa.Integer),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.Text),
        sa.Column('path', sa.String, nullable=False),
        sa.Column('type', sa.String, nullable=False),
        sa.Column('mime_type', sa.String, nullable=False),

        sa.Column('created_at', sa.DateTime(), default=datetime.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=True),

        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['application_id'], ['applications.id'], None, 'CASCADE', 'CASCADE'),
    )


def downgrade():
    op.drop_table('attachments')
