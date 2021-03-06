"""for_other

Revision ID: 8384170fcd04
Revises: 3da80373e7ab
Create Date: 2016-11-27 20:39:11.551350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8384170fcd04'
down_revision = '3da80373e7ab'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('create_project', sa.Column('c_abstract', sa.Text(), nullable=True))
    op.add_column('create_project', sa.Column('c_of_class', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('c_other_stu', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('c_project_category', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('c_project_level', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('c_project_name', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('c_project_number', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('c_stu_class', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('c_stu_count', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('c_stu_name', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('c_stu_number', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('c_stu_phone', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('c_stu_qq', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('c_teacher_name', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('c_teacher_title', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('c_year', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('filename', sa.String(length=64), nullable=True))
    op.add_column('create_project', sa.Column('stu_academy', sa.String(length=64), nullable=True))
    op.add_column('other', sa.Column('award_department', sa.String(length=64), nullable=True))
    op.add_column('other', sa.Column('filename', sa.String(length=64), nullable=True))
    op.add_column('other', sa.Column('head_class', sa.String(length=64), nullable=True))
    op.add_column('other', sa.Column('head_number', sa.String(length=64), nullable=True))
    op.add_column('other', sa.Column('head_phone', sa.String(length=64), nullable=True))
    op.add_column('other', sa.Column('head_qq', sa.String(length=64), nullable=True))
    op.add_column('other', sa.Column('prize_category', sa.String(length=64), nullable=True))
    op.add_column('other', sa.Column('prize_date', sa.String(length=64), nullable=True))
    op.add_column('other', sa.Column('prize_level', sa.String(length=64), nullable=True))
    op.add_column('other', sa.Column('prize_name', sa.String(length=64), nullable=True))
    op.add_column('other', sa.Column('prize_personage_collective', sa.String(length=64), nullable=True))
    op.add_column('other', sa.Column('stu_academy', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('other', 'stu_academy')
    op.drop_column('other', 'prize_personage_collective')
    op.drop_column('other', 'prize_name')
    op.drop_column('other', 'prize_level')
    op.drop_column('other', 'prize_date')
    op.drop_column('other', 'prize_category')
    op.drop_column('other', 'head_qq')
    op.drop_column('other', 'head_phone')
    op.drop_column('other', 'head_number')
    op.drop_column('other', 'head_class')
    op.drop_column('other', 'filename')
    op.drop_column('other', 'award_department')
    op.drop_column('create_project', 'stu_academy')
    op.drop_column('create_project', 'filename')
    op.drop_column('create_project', 'c_year')
    op.drop_column('create_project', 'c_teacher_title')
    op.drop_column('create_project', 'c_teacher_name')
    op.drop_column('create_project', 'c_stu_qq')
    op.drop_column('create_project', 'c_stu_phone')
    op.drop_column('create_project', 'c_stu_number')
    op.drop_column('create_project', 'c_stu_name')
    op.drop_column('create_project', 'c_stu_count')
    op.drop_column('create_project', 'c_stu_class')
    op.drop_column('create_project', 'c_project_number')
    op.drop_column('create_project', 'c_project_name')
    op.drop_column('create_project', 'c_project_level')
    op.drop_column('create_project', 'c_project_category')
    op.drop_column('create_project', 'c_other_stu')
    op.drop_column('create_project', 'c_of_class')
    op.drop_column('create_project', 'c_abstract')
    ### end Alembic commands ###
