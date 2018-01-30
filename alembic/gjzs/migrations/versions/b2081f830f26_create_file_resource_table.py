"""create file resource table

Revision ID: b2081f830f26
Revises: 3db61e55d93a
Create Date: 2017-07-20 15:04:06.704044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2081f830f26'
down_revision = '3db61e55d93a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            't_dgap_file_resource',
            sa.Column('id',sa.String,primary_key=True),
            )

def downgrade():
    pass
