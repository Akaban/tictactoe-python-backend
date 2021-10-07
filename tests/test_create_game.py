def test_create_game(app):
    response = app.test_client().post('api/games')

    keys = {"game_id", "current_player", "is_over", "winner", "grid"}

    assert response.status_code == 200
    assert set(response.json.keys()) == keys
    assert response.json["grid"] == "-"*9