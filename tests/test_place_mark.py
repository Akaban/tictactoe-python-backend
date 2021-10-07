def test_no_duplicate_mark(app):

    response_create_game = app.test_client().post("api/games")
    game_id = response_create_game.json["game_id"]

    response_patch_1 = app.test_client().patch(f"api/games/{game_id}", json={"row": 0, "col": 0, "player": "X"})
    response_patch_2 = app.test_client().patch(f"api/games/{game_id}", json={"row": 0, "col": 0, "player": "O"})

    assert response_patch_1.status_code == 200
    assert response_patch_2.status_code == 400

def test_no_double_move(app):

    response_create_game = app.test_client().post("api/games")
    game_id = response_create_game.json["game_id"]

    response_patch_1 = app.test_client().patch(f"api/games/{game_id}", json={"row": 0, "col": 0, "player": "X"})
    response_patch_2 = app.test_client().patch(f"api/games/{game_id}", json={"row": 1, "col": 0, "player": "X"})

    assert response_patch_1.status_code == 200
    assert response_patch_2.status_code == 400


def test_grid_update_logic(app):

    for row, col in zip(range(3), range(3)):
        response_create_game = app.test_client().post("api/games")
        game_id = response_create_game.json["game_id"]

        response_patch = app.test_client().patch(
            f"api/games/{game_id}",json={"row": row, "col": col, "player": "X"}
            )

        assert response_patch.status_code == 200

        grid = response_patch.json["grid"]

        assert grid[col*3+row] == 'X'


def test_game_is_over(app):

    games = (
        ([(0,0), (2,0), (0, 1), (2, 1), (0, 2)], "X"), # X won
        ([(0, 0), (2, 2), (1, 0)], None), # No one won
    )

    for game in games:
        moves, outcome = game

        response_create_game = app.test_client().post("api/games")
        game_id = response_create_game.json["game_id"]

        current_player = 'X'

        for move_col, move_row in moves:
            response_patch = app.test_client().patch(
            f"api/games/{game_id}",json={"row": move_row, "col": move_col, "player": current_player}
            )

            assert response_patch.status_code == 200

            if current_player == 'X':
                current_player = 'O'
            elif current_player == 'O':
                current_player = 'X'

        response_get_game = app.test_client().get(f"api/games/{game_id}")

        if outcome == 'X':
            assert response_get_game.json["is_over"]
            assert response_get_game.json["winner"] == 'X'
        elif outcome is None:
            assert not response_get_game.json["is_over"]








