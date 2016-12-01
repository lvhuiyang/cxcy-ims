"""update_for_competition

Revision ID: a149759b0d47
Revises: 186c5830e2c2
Create Date: 2016-11-30 21:56:16.981011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a149759b0d47'
down_revision = '186c5830e2c2'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('competitions', sa.Column('stu_academy', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('competitions', 'stu_academy')
    ### end Alembic commands ###
