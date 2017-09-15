"""empty message

Revision ID: 96529e3fe19e
Revises: bcede08815ab
Create Date: 2017-07-31 17:34:02.190200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96529e3fe19e'
down_revision = 'bcede08815ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('title', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_posts_title'), 'posts', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_title'), table_name='posts')
    op.drop_column('posts', 'title')
    # ### end Alembic commands ###
