from sqlalchemy import Double, Enum, ForeignKey, Table, Column, Text, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from src.database.execution import db_client

# Reusing the status_enum defined in your snippet
status_enum = Enum(
    'active', 'disabled', 'in_progress', 'arrived', 
    'under_maintenance', 'delayed', 
    name="status"
)

trip_history = Table(
    "trip_history",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid),
    Column("trip_id", UUID(as_uuid=True), ForeignKey("trips.id")),
    Column("delay_minutes", Integer), # Labels for Classification/Regression
    Column("traffic_level", Text),    # Features for ETA
    Column("weather_condition", Text),# Features for ETA
    Column("created_at", DateTime, nullable=False, **db_client.default_now),
)