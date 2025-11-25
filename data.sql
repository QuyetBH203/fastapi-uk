CREATE TYPE employee_status AS ENUM ('ACTIVE', 'NOT_STARTED', 'TERMINATED');

CREATE TABLE organizations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    code VARCHAR(50) UNIQUE NOT NULL,  
    column_config JSONB NOT NULL DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);


CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    organization_id INT NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,

    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,

    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(50),

    department VARCHAR(100),
    location VARCHAR(100),
    company VARCHAR(100),
    position VARCHAR(100),
    status employee_status NOT NULL DEFAULT 'ACTIVE',

    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
