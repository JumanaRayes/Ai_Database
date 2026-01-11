from sqlalchemy import Boolean, Double, Enum, ForeignKey, Table, Column, Text, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from src.database.execution import db_client


student_boarding_logs = Table(
    "student_boarding_logs",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid),
    Column("student_id", UUID(as_uuid=True), ForeignKey("students.id")),
    Column("stop_id", UUID(as_uuid=True), ForeignKey("stops.id")),
    Column("trip_id", UUID(as_uuid=True), ForeignKey("trips.id")),
    Column("boarded_at", DateTime, **db_client.default_now),
    Column("is_no_show", Boolean, default=False), 
    Column("created_at", DateTime, nullable=False, **db_client.default_now),
)