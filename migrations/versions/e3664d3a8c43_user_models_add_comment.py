"""user models add comment

Revision ID: e3664d3a8c43
Revises: a4ac94863d40
Create Date: 2016-11-22 21:01:27.874199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3664d3a8c43'
down_revision = 'a4ac94863d40'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('comment', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'comment')
    ### end Alembic commands ###
