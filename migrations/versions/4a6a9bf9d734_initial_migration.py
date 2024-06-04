"""Initial migration.

Revision ID: 4a6a9bf9d734
Revises: 261bf3eecc7f
Create Date: 2024-06-04 22:53:30.672720

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4a6a9bf9d734'
down_revision = '261bf3eecc7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('email', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('join_date', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('user_role', sa.Enum('ADMIN', 'USER', name='userrole'), nullable=True))
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.drop_column('is_admin')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('password',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.drop_column('user_role')
        batch_op.drop_column('join_date')
        batch_op.drop_column('active')
        batch_op.drop_column('email')
        batch_op.drop_column('name')

    # ### end Alembic commands ###