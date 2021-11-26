from app import app

def test1():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test2():
    response = app.test_client().get('/edit')
    assert response.status_code == 200

def test3():
    response = app.test_client().get('/edit')
    assert b"Todo app" in response.data
    assert b"Todo title" in response.data
    assert b"Add" in response.data
