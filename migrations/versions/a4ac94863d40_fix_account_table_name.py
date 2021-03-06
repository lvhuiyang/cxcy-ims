"""fix account table name

Revision ID: a4ac94863d40
Revises: 972327f5fa84
Create Date: 2016-11-21 20:09:34.783710

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a4ac94863d40'
down_revision = '972327f5fa84'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('real_name', sa.String(length=32), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('power', sa.Integer(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('created_people', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_real_name'), 'users', ['real_name'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.drop_table('accounts')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('username', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('real_name', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('password_hash', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('power', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('created_date', mysql.DATETIME(), nullable=True),
    sa.Column('created_people', mysql.VARCHAR(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_real_name'), table_name='users')
    op.drop_table('users')
    ### end Alembic commands ###
