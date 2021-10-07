def test_get_version(app):
    response = app.test_client().get('api/version')
    assert response.status_code == 200
    assert response.json == {"version": 1.0}
