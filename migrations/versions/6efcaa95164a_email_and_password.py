"""email and password

Revision ID: 6efcaa95164a
Revises: 93eda90022df
Create Date: 2019-01-31 12:25:22.503031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6efcaa95164a'
down_revision = '93eda90022df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_name'), table_name='users')
    # ### end Alembic commands ###