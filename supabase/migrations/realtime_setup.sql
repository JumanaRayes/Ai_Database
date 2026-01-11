-- 1. Start a transaction to ensure all changes happen together
BEGIN;

  -- 2. Clean up any old publication settings
  DROP PUBLICATION IF EXISTS supabase_realtime;
  
  -- 3. Define which tables broadcast live events
  -- This is critical for the BusBot to 'see' updates as they happen
  CREATE PUBLICATION supabase_realtime FOR TABLE 
    trips,          -- To update bus markers on the map
    bus_location,   -- To show students if the bus is full
    stops,          -- To update stop status (e.g., 'Delayed')
    stop_arrivals;  -- To notify BusBot of exactly when a bus hits a stop

COMMIT;

-- 4. Security Check: Enable 'Replica Identity' 
-- This ensures the 'OLD' data and 'NEW' data are both sent in the update
ALTER TABLE trips REPLICA IDENTITY FULL;
ALTER TABLE bus_location REPLICA IDENTITY FULL;