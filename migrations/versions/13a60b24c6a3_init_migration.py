"""init migration

Revision ID: 13a60b24c6a3
Revises: 
Create Date: 2016-11-19 15:41:49.087350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13a60b24c6a3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('name', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('projects', 'name')
    ### end Alembic commands ###
