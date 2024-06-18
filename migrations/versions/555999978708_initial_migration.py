"""Initial migration.

Revision ID: 555999978708
Revises: 5dc66de2c6e5
Create Date: 2024-06-05 06:10:09.575529

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '555999978708'
down_revision = '5dc66de2c6e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###