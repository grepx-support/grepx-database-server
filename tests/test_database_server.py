import setup_test_paths

import pytest
from database_server import DatabaseServer
from pathlib import Path

@pytest.mark.asyncio
async def test_database_server_initialize(master_db_config, test_data_dir):
    config_path = test_data_dir / "test_config.yaml"
    
    import yaml
    config_data = {
        'master_db': {
            'enabled': True,
            'type': 'sqlite',
            'connection_string': master_db_config['connection_string']
        },
        'server': {
            'host': '0.0.0.0',
            'port': 8000
        },
        'logging': {
            'level': 'INFO'
        }
    }
    
    with open(config_path, 'w') as f:
        yaml.dump(config_data, f)
    
    server = DatabaseServer(config_path=str(config_path))
    
    await server.initialize()
    
    assert server.master_db is not None
    assert len(server.read_service._sessions) > 0
    assert len(server.write_service._sessions) > 0
    
    await server.shutdown()
    
    config_path.unlink()

@pytest.mark.asyncio
async def test_database_server_get_backend(master_db_config, test_data_dir):
    config_path = test_data_dir / "test_config.yaml"
    
    import yaml
    config_data = {
        'master_db': {
            'enabled': True,
            'type': 'sqlite',
            'connection_string': master_db_config['connection_string']
        },
        'server': {
            'host': '0.0.0.0',
            'port': 8000
        },
        'logging': {
            'level': 'INFO'
        }
    }
    
    with open(config_path, 'w') as f:
        yaml.dump(config_data, f)
    
    server = DatabaseServer(config_path=str(config_path))
    await server.initialize()
    
    read_backend = server.read_service.get_backend('test_sqlite_db')
    assert read_backend is not None
    
    write_backend = server.write_service.get_backend('test_sqlite_db')
    assert write_backend is not None
    
    await server.shutdown()
    config_path.unlink()
