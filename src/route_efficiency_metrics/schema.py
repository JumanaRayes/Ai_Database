from sqlalchemy import Double, Enum, ForeignKey, Table, Column, Text, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from src.database.execution import db_client

status_enum = Enum(
    'active', 'disabled', 'in_progress', 'arrived', 
    'under_maintenance', 'delayed', 
    name="status"
)

route_efficiency_metrics = Table(
    "route_efficiency_metrics",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid),
    Column("route_id", UUID(as_uuid=True), ForeignKey("routes.id")),
    Column("efficiency_score", Double),
    Column("avg_delay_minutes", Double),
    Column("peak_occupancy_rate", Double), 
    Column("calculation_date", DateTime, **db_client.default_now),
)