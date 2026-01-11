-- Enable RLS on core tables
ALTER TABLE students ENABLE ROW LEVEL SECURITY;
ALTER TABLE trips ENABLE ROW LEVEL SECURITY;

-- 1. Students can only read their own profile
CREATE POLICY student_self_access ON students
    FOR SELECT USING (auth.uid() = id);

-- 2. Everyone can read live trip locations (Public/Authenticated)
CREATE POLICY public_trip_tracking ON trips
    FOR SELECT TO authenticated USING (true);

-- 3. Only Admins can view efficiency metrics
CREATE POLICY admin_only_metrics ON route_efficiency_metrics
    FOR ALL TO authenticated 
    USING (EXISTS (SELECT 1 FROM admin WHERE admin.id = auth.uid()));