"""user info

Revision ID: 8306cb2b9267
Revises: 8af882b3d698
Create Date: 2019-02-09 13:08:18.274011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8306cb2b9267'
down_revision = '8af882b3d698'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(), nullable=True))
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.drop_index('ix_users_name', table_name='users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_users_name', 'users', ['name'], unique=1)
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###