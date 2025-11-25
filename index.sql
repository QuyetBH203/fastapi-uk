
CREATE INDEX IF NOT EXISTS idx_employees_organization ON employees (organization_id);

CREATE INDEX IF NOT EXISTS idx_employees_status ON employees (status);

CREATE INDEX IF NOT EXISTS idx_employees_department ON employees (department);
CREATE INDEX IF NOT EXISTS idx_employees_location ON employees (location);
CREATE INDEX IF NOT EXISTS idx_employees_position ON employees (position);

CREATE INDEX IF NOT EXISTS idx_employees_email ON employees (email);

CREATE INDEX IF NOT EXISTS idx_employees_name ON employees (last_name, first_name);

CREATE EXTENSION IF NOT EXISTS pg_trgm;

CREATE INDEX IF NOT EXISTS idx_employees_name_trgm 
    ON employees USING gin ((first_name || ' ' || last_name) gin_trgm_ops);

CREATE INDEX IF NOT EXISTS idx_employees_email_trgm 
    ON employees USING gin (email gin_trgm_ops);
