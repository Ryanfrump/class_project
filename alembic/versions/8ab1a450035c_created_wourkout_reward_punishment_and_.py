"""created wourkout, reward, punishment, and days tables

Revision ID: 8ab1a450035c
Revises: 
Create Date: 2024-04-30 10:48:33.560599

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '8ab1a450035c'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('days',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('last_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workout',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('set', sa.Integer(), nullable=False),
    sa.Column('rep', sa.Integer(), nullable=False),
    sa.Column('help_video', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('punishment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('punishment_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('punishment', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('punishment_item', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['punishment_item'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reward',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('item_value', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('user_item', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_item'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reward')
    op.drop_table('punishment')
    op.drop_table('workout')
    op.drop_table('user')
    op.drop_table('days')
    # ### end Alembic commands ###