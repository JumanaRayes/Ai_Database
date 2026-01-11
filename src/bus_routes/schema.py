from sqlalchemy import Enum, Table, Column, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from src.database.execution import db_client

status_enum = Enum(
    'active', 'disabled', 'in_progress', 'arrived', 
    'under_maintenance', 'delayed', 
    name="status"
)

routes = Table(
    "routes",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid),
    Column("name", Text),
    Column("status", status_enum),
    Column("created_at", DateTime, nullable=False, **db_client.default_now),
)