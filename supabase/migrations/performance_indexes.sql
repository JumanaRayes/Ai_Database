-- 1. Enable Required Extensions for Spatial AI
CREATE EXTENSION IF NOT EXISTS cube;
CREATE EXTENSION IF NOT EXISTS earthdistance;

-- 2. Index for Spatial Queries (ETA Prediction)
-- This allows the AI to calculate "Distance to Stop" in milliseconds
-- We use a functional index on the lat/long columns
CREATE INDEX idx_trips_location 
ON trips USING gist (ll_to_earth(latitude, longitude));

-- 3. Index for Historical Analysis (Delay Classification)
-- AI needs to scan history by route to find patterns (e.g., "Monday morning delays")
CREATE INDEX idx_trip_history_route_time 
ON trip_history (route_id, created_at DESC);

-- 4. Index for Foreign Keys (Join Performance)
-- These ensure that joining 'trips' to 'stop_arrivals' doesn't slow down as data grows
CREATE INDEX idx_stop_arrivals_trip_id ON stop_arrivals (trip_id);
CREATE INDEX idx_stop_arrivals_stop_id ON stop_arrivals (stop_id);
CREATE INDEX idx_boarding_logs_student_id ON student_boarding_logs (student_id);

-- 5. Index for Real-time Search
-- Helps the BusBot find a student by their ID instantly
CREATE INDEX idx_students_student_id_hash ON students USING hash (student_id);