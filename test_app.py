import pytest
from app import app  # adjust this import to the name of your Flask app file

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_books(client):
    """Test retrieving all books."""
    response = client.get('/books')
    assert response.status_code == 200
    assert len(response.json) == 3  # Adjust based on your initial data

def test_get_book(client):
    """Test retrieving a specific book by ID."""
    response = client.get('/books/1')
    assert response.status_code == 200
    assert response.json['title'] == 'Harry Potter'

def test_add_book(client):
    """Test adding a new book."""
    new_book = {"id": 4, "title": "A Game of Thrones", "author": "George R.R. Martin"}
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    assert response.json == {'message': 'Book added successfully'}

def test_update_book(client):
    """Test updating an existing book."""
    updated_data = {"title": "Harry Potter and the Chamber of Secrets"}
    response = client.put('/books/1', json=updated_data)
    assert response.status_code == 200
    assert response.json == {'message': 'Book updated successfully'}

def test_delete_book(client):
    """Test deleting a book."""
    response = client.delete('/books/1')
    assert response.status_code == 200
    assert response.json == {'message': 'Book deleted successfully'}
