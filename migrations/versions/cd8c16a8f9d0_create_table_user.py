"""create table user

Revision ID: cd8c16a8f9d0
Revises: eaae517c1e2f
Create Date: 2022-07-30 15:13:41.385357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd8c16a8f9d0'
down_revision = 'eaae517c1e2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=50), nullable=True),
    sa.Column('middleName', sa.String(length=50), nullable=True),
    sa.Column('lastName', sa.String(length=50), nullable=False),
    sa.Column('mobile', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('passwordHash', sa.String(length=100), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.Column('vendor', sa.Boolean(), nullable=True),
    sa.Column('registeredAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('lastLogin', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('intro', sa.String(), nullable=True),
    sa.Column('profile', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=75), nullable=False),
    sa.Column('metaTitle', sa.String(length=100), nullable=True),
    sa.Column('slug', sa.String(length=100), nullable=True),
    sa.Column('summary', sa.String(), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('sku', sa.String(length=100), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('discount', sa.Float(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('shop', sa.Boolean(), nullable=True),
    sa.Column('createdAt', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updatedAt', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('publishedAt', sa.DateTime(), nullable=True),
    sa.Column('startsAt', sa.DateTime(), nullable=True),
    sa.Column('endsAt', sa.DateTime(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_id'), 'product', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_id'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###