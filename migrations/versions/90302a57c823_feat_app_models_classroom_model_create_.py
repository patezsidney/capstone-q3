"""feat(app.models.classroom_model): create table ClassroomModels

Revision ID: 90302a57c823
Revises: 
Create Date: 2022-03-02 13:26:53.535956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90302a57c823'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classroom_model',
    sa.Column('classroom', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('classroom')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('classroom_model')
    # ### end Alembic commands ###
