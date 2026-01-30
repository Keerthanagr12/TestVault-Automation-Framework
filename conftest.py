"""pytest configuration and global fixtures"""
import os
import sys
import json
from pathlib import Path

import pytest
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))


class Config:
    """Test Configuration"""
    # API Configuration
    BASE_URL = os.getenv('BASE_URL', 'https://api.example.com')
    TIMEOUT = int(os.getenv('TIMEOUT', '10'))
    RETRY_COUNT = int(os.getenv('RETRY_COUNT', '3'))
    
    # Paths
    ROOT_DIR = Path(__file__).parent
    CONFIG_DIR = ROOT_DIR / 'config'
    TESTS_DIR = ROOT_DIR / 'tests'
    REPORTS_DIR = ROOT_DIR / 'reports'
    
    # Ensure directories exist
    REPORTS_DIR.mkdir(exist_ok=True)


@pytest.fixture(scope='session')
def config():
    """Session-level config fixture"""
    return Config


@pytest.fixture(scope='session')
def test_data():
    """Load test data from JSON file"""
    test_data_file = Config.CONFIG_DIR / 'test_data.json'
    if test_data_file.exists():
        with open(test_data_file) as f:
            return json.load(f)
    return {}


@pytest.fixture(scope='function', autouse=True)
def reset_test_state():
    """Reset test state before each test"""
    yield
    # Cleanup after test
    pass


# pytest hooks
def pytest_configure(config):
    """Configure pytest"""
    config.addinivalue_line('markers', 'integration: mark test as integration')
    config.addinivalue_line('markers', 'api: mark test as api')


def pytest_collection_modifyitems(config, items):
    """Modify collected test items"""
    for item in items:
        # Add markers based on test path
        if 'integration' in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif 'api' in str(item.fspath):
            item.add_marker(pytest.mark.api)
