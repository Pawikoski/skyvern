"""add ai_suggestions table

Revision ID: d5640aa644b9
Revises: d47a586d7036
Create Date: 2025-01-09 05:41:43.872901+00:00

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d5640aa644b9"
down_revision: Union[str, None] = "d47a586d7036"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "ai_suggestions",
        sa.Column("ai_suggestion_id", sa.String(), nullable=False),
        sa.Column("organization_id", sa.String(), nullable=True),
        sa.Column("ai_suggestion_type", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organizations.organization_id"],
        ),
        sa.PrimaryKeyConstraint("ai_suggestion_id"),
    )
    op.add_column("artifacts", sa.Column("ai_suggestion_id", sa.String(), nullable=True))
    op.create_index(op.f("ix_artifacts_ai_suggestion_id"), "artifacts", ["ai_suggestion_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_artifacts_ai_suggestion_id"), table_name="artifacts")
    op.drop_column("artifacts", "ai_suggestion_id")
    op.drop_table("ai_suggestions")
    # ### end Alembic commands ###
