from sqlalchemy import Double, Enum, ForeignKey, Integer, Table, Column, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from src.database.execution import db_client

status_enum = Enum(
    'active', 'disabled', 'in_progress', 'arrived', 
    'under_maintenance', 'delayed', 
    name="status"
)

stops = Table(
    "stops",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid),
    Column("route_id", UUID(as_uuid=True), ForeignKey("routes.id")),
    Column("name", Text),
    Column("latitude", Double),
    Column("longitude", Double),
    Column("stop_sequence", Integer), # CRITICAL for AI to know the order of stops
    Column("status", status_enum),
)