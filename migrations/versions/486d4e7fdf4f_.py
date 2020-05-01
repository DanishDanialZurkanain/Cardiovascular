"""empty message

Revision ID: 486d4e7fdf4f
Revises: 1bc986bb2aca
Create Date: 2020-05-01 12:48:37.768341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '486d4e7fdf4f'
down_revision = '1bc986bb2aca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'hashCode')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hashCode', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    # ### end Alembic commands ###