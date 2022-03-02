"""merging two heads

Revision ID: b00c35cdbdda
Revises: 27094b5f2378, e0fca0a53be4, a87d06572468, bc30491f0052
Create Date: 2022-03-02 15:23:45.829829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b00c35cdbdda'
down_revision = ('27094b5f2378', 'e0fca0a53be4', 'a87d06572468', 'bc30491f0052')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
