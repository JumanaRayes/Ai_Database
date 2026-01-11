from sqlalchemy import Double, Enum, ForeignKey, Table, Column, Text, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from src.database.execution import db_client


status_enum = Enum(
    'active', 'disabled', 'in_progress', 'arrived', 
    'under_maintenance', 'delayed', 
    name="status"
)

stop_arrivals = Table(
    "stop_arrivals",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid),
    Column("trip_id", UUID(as_uuid=True), ForeignKey("trips.id")),
    Column("stop_id", UUID(as_uuid=True), ForeignKey("stops.id")),
    Column("planned_arrival_time", DateTime),
    Column("actual_arrival_time", DateTime),
    Column("arrival_delay_seconds", Double),
    Column("dwell_time_seconds", Double), 
)