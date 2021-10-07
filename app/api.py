from .extensions import *

def get_version():
    return {"version": 1.0}


def create_game():
    game = Game(is_over=False, grid=DEFAULT_GRID)
    db.session.add(game)
    db.session.commit()

    return game.as_dict()


def get_game(game_id):
    game = Game.query.get(game_id)

    if game is None:
        return {"message": "No game found."}, 404
    return game.as_dict()


def place_mark(game_id, mark):
    INVALID_INPUT = {"message": "Invalid input or can't place mark here"}, 400


    game = Game.query.get(game_id)

    if game is None:
        return {"message": "No game found."}, 404

    if game.is_over or (game.current_player != mark["player"] and game.current_player is not None):
        return INVALID_INPUT

    mark_index = mark["col"] * 3 + mark["row"]

    grid = getattr(game, "grid")

    if grid[mark_index] != "-":
        return INVALID_INPUT

    grid = f"{grid[:mark_index]}{mark['player']}{grid[mark_index + 1:]}"

    setattr(game, "grid", grid)

    game.update_is_over()
    game.switch_player(current_player=mark["player"])
    

    db.session.commit()

    return {
        "message": f"Congratulations player {mark['player']} you won the game!"
        if game.is_over else "Mark placed.",
        **game.as_dict()
        }

