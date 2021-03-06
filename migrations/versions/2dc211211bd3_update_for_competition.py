"""update_for_competition

Revision ID: 2dc211211bd3
Revises: a149759b0d47
Create Date: 2016-12-01 11:38:48.323033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dc211211bd3'
down_revision = 'a149759b0d47'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('competitions', sa.Column('project_name', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('competitions', 'project_name')
    ### end Alembic commands ###
