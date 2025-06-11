import os
import tempfile
import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    test_dir = tempfile.mkdtemp()
    app.config['FILES_DIRECTORY'] = test_dir  # surcharge pour les tests
    with open(os.path.join(test_dir, 'testfile.txt'), 'w') as f:
        f.write('Hello World')
    yield app.test_client()
    for file in os.listdir(test_dir):
        os.remove(os.path.join(test_dir, file))
    os.rmdir(test_dir)

def test_api_files(client):
    response = client.get('/api/files')
    assert response.status_code == 200
    assert 'testfile.txt' in response.json

def test_download_file(client):
    response = client.get('/download/testfile.txt')
    assert response.status_code == 200
    assert b'Hello World' in response.data

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'testfile.txt' in response.data
