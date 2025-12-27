"""add server default to project.created_at

Revision ID: 2e2db204b6e7
Revises: 9a90be9fe4fe
Create Date: 2025-12-17 18:20:29.401464

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e2db204b6e7'
down_revision: Union[str, Sequence[str], None] = '9a90be9fe4fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "project",
        "created_at",
        existing_type=sa.DateTime(),
        server_default=sa.func.now(),
        nullable=False
    )
    op.alter_column(
        "issue",
        "created_at",
        existing_type=sa.DateTime(),
        server_default=sa.func.now(),
        nullable=False
    )

def downgrade() -> None:
    """Downgrade schema."""
    pass
