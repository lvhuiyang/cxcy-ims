"""update for submit_history

Revision ID: 55d3df24d613
Revises: 8384170fcd04
Create Date: 2016-11-28 15:14:21.061821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55d3df24d613'
down_revision = '8384170fcd04'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('submit_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('submit_content', sa.String(length=64), nullable=True),
    sa.Column('filename', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('submit_history')
    ### end Alembic commands ###