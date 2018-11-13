"""empty message

Revision ID: 8bc36e1a8169
Revises: ccd0a3bf0622
Create Date: 2018-10-27 18:24:40.712443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bc36e1a8169'
down_revision = 'ccd0a3bf0622'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shark_projections',
    sa.Column('segment', sa.Integer(), nullable=False),
    sa.Column('scoring', sa.Integer(), nullable=False),
    sa.Column('player', sa.String(length=64), nullable=False),
    sa.Column('team', sa.String(length=8), nullable=False),
    sa.Column('points', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('segment', 'scoring', 'player', 'team')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shark_projections')
    # ### end Alembic commands ###