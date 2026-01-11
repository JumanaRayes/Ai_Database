from sqlalchemy import Table, Column, Text, Integer, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from src.database.execution import db_client

status_enum = Enum(
    'active', 'disabled', 'in_progress', 'arrived', 
    'under_maintenance', 'delayed', 
    name="status"
)

buses = Table(
    "buses",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid),
    Column("bus_number", Integer, unique=True),
    Column("capacity_total", Integer), # AI needs this to calculate occupancy %
    Column("status", status_enum),
    Column("created_at", DateTime, nullable=False, **db_client.default_now),
    Column("updated_at", DateTime, nullable=False, onupdate=db_client.now, **db_client.default_now),
) 