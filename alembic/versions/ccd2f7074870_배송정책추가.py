"""배송정책추가

Revision ID: ccd2f7074870
Revises: 4f80ea9b894b
Create Date: 2019-06-27 05:11:07.086687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccd2f7074870'
down_revision = '4f80ea9b894b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('can_bundle', sa.Boolean(), nullable=True))
    op.add_column('products', sa.Column('shipping_price', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'shipping_price')
    op.drop_column('products', 'can_bundle')
    # ### end Alembic commands ###
