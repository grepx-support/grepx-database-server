import setup_test_paths

import pytest
from dbManager import BaseMasterDBManager

@pytest.mark.asyncio
async def test_master_db_connect(master_db_config):
    manager = BaseMasterDBManager(master_db_config)
    
    await manager.connect()
    
    assert manager.session is not None
    assert manager.db_type == 'sqlite'
    
    await manager.disconnect()

@pytest.mark.asyncio
async def test_get_all_active_storages(master_db_config):
    manager = BaseMasterDBManager(master_db_config)
    await manager.connect()
    
    storages = await manager.get_all_active_storages()
    
    assert len(storages) > 0
    assert all(storage['active_flag'] for storage in storages)
    
    storage_names = [s['storage_name'] for s in storages]
    assert 'test_postgres_db' in storage_names
    assert 'test_sqlite_db' in storage_names
    
    await manager.disconnect()

@pytest.mark.asyncio
async def test_get_storage_by_name(master_db_config):
    manager = BaseMasterDBManager(master_db_config)
    await manager.connect()
    
    storage = await manager.get_storage_by_name('test_sqlite_db')
    
    assert storage is not None
    assert storage['storage_name'] == 'test_sqlite_db'
    assert storage['storage_type'] == 'sqlite'
    assert storage['active_flag'] == 1
    
    await manager.disconnect()

@pytest.mark.asyncio
async def test_get_default_storage(master_db_config):
    manager = BaseMasterDBManager(master_db_config)
    await manager.connect()
    
    storage = await manager.get_default_storage()
    
    assert storage is not None
    assert storage['is_default'] == 1
    assert storage['storage_name'] == 'test_postgres_db'
    
    await manager.disconnect()

@pytest.mark.asyncio
async def test_get_storages_by_type(master_db_config):
    manager = BaseMasterDBManager(master_db_config)
    await manager.connect()
    
    storages = await manager.get_storages_by_type('sqlite')
    
    assert len(storages) > 0
    assert all(s['storage_type'] == 'sqlite' for s in storages)
    
    await manager.disconnect()

@pytest.mark.asyncio
async def test_storage_not_found(master_db_config):
    manager = BaseMasterDBManager(master_db_config)
    await manager.connect()
    
    storage = await manager.get_storage_by_name('nonexistent_db')
    
    assert storage is None
    
    await manager.disconnect()
