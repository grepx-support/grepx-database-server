import setup_test_paths

import pytest
import asyncio
import sqlite3
from pathlib import Path

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
def test_data_dir():
    test_dir = Path(__file__).parent / "test_data"
    test_dir.mkdir(exist_ok=True)
    return test_dir

@pytest.fixture(scope="session")
def master_db_path(test_data_dir):
    db_path = test_data_dir / "master.db"
    
    if db_path.exists():
        db_path.unlink()
    
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    sql_file = test_data_dir / "init_master_db.sql"
    with open(sql_file, 'r') as f:
        sql_script = f.read()
    
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    
    yield db_path
    
    if db_path.exists():
        db_path.unlink()

@pytest.fixture(scope="session")
def test_sqlite_db_path(test_data_dir):
    db_path = test_data_dir / "test.db"
    
    if db_path.exists():
        db_path.unlink()
    
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age INTEGER
        )
    """)
    
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
                   ("Alice", "alice@test.com", 30))
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
                   ("Bob", "bob@test.com", 25))
    
    conn.commit()
    conn.close()
    
    yield db_path
    
    if db_path.exists():
        db_path.unlink()

@pytest.fixture
def master_db_config(master_db_path):
    return {
        'type': 'sqlite',
        'connection_string': f'sqlite:///{master_db_path}'
    }
