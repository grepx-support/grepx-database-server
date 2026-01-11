CREATE TABLE IF NOT EXISTS storage_master (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    storage_name TEXT NOT NULL UNIQUE,
    storage_type TEXT NOT NULL,
    host TEXT,
    port INTEGER,
    database_name TEXT,
    username TEXT,
    password TEXT,
    connection_string TEXT,
    file_path TEXT,
    auth_source TEXT,
    ssl_enabled INTEGER DEFAULT 0,
    connection_params TEXT,
    credentials TEXT,
    storage_metadata TEXT,
    is_default INTEGER DEFAULT 0,
    active_flag INTEGER DEFAULT 1,
    max_connections INTEGER DEFAULT 10,
    timeout_seconds INTEGER DEFAULT 30,
    description TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by TEXT,
    updated_by TEXT
);

INSERT INTO storage_master (
    storage_name, storage_type, host, port, database_name, 
    username, password, active_flag, is_default, max_connections
) VALUES 
(
    'test_postgres_db',
    'postgresql',
    'localhost',
    5432,
    'test_db',
    'test_user',
    'test_pass',
    1,
    1,
    10
),
(
    'test_sqlite_db',
    'sqlite',
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    1,
    0,
    5
);

UPDATE storage_master 
SET file_path = './tests/test_data/test.db' 
WHERE storage_name = 'test_sqlite_db';

UPDATE storage_master 
SET connection_string = 'postgresql://test_user:test_pass@localhost:5432/test_db' 
WHERE storage_name = 'test_postgres_db';

UPDATE storage_master 
SET connection_string = 'sqlite:///./tests/test_data/test.db' 
WHERE storage_name = 'test_sqlite_db';
