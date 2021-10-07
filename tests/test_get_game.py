def test_get_game(app):

    response_create_game = app.test_client().post("api/games")
    create_game_id = response_create_game.json["game_id"]
    response_get_game = app.test_client().get(f"api/games/{create_game_id}")

    assert response_get_game.status_code == 200
    assert response_create_game.json == response_get_game.json