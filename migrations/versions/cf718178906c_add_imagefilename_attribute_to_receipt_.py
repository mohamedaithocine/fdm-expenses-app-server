"""Add imageFileName attribute to Receipt model

Revision ID: cf718178906c
Revises: 6fc382141939
Create Date: 2024-04-09 21:36:45.741935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf718178906c'
down_revision = '6fc382141939'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('receipt', schema=None) as batch_op:
        batch_op.add_column(sa.Column('imageFileName', sa.String(length=144), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('receipt', schema=None) as batch_op:
        batch_op.drop_column('imageFileName')

    # ### end Alembic commands ###
