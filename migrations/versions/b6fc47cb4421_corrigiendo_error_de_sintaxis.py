"""Corrigiendo error de sintaxis

Revision ID: b6fc47cb4421
Revises: a5cffa318ac2
Create Date: 2025-03-17 22:04:20.093159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6fc47cb4421'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('birth_year', sa.String(length=20), nullable=False),
    sa.Column('eye_color', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('hair_color', sa.String(length=20), nullable=False),
    sa.Column('height', sa.String(length=20), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('climate', sa.String(length=20), nullable=False),
    sa.Column('rotation_time', sa.String(length=20), nullable=False),
    sa.Column('diameter', sa.String(length=20), nullable=False),
    sa.Column('gravity', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('model', sa.String(length=20), nullable=False),
    sa.Column('vehicle_type', sa.String(length=20), nullable=False),
    sa.Column('length', sa.String(length=20), nullable=False),
    sa.Column('value', sa.String(length=20), nullable=False),
    sa.Column('fuel_capacity', sa.String(length=20), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('characters_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['characters_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=40), nullable=False))
        batch_op.add_column(sa.Column('firstname', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('lastname', sa.String(length=20), nullable=False))
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=25),
               existing_nullable=False)
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('password',
               existing_type=sa.String(length=25),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.drop_column('lastname')
        batch_op.drop_column('firstname')
        batch_op.drop_column('username')

    op.drop_table('favorite')
    op.drop_table('vehicles')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###
