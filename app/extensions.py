from flask_sqlalchemy import SQLAlchemy

from toolz.itertoolz import partition

db = SQLAlchemy()

DEFAULT_GRID = '-'*9

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/lc-test.db'
    db.init_app(app)


class Game(db.Model):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def switch_player(self, current_player=None):
        if self.current_player is None:
            if current_player is None:
                raise Exception("current_player is None, you must specify it.")
            if current_player not in ('X', 'O'):
                raise Exception("current_player provided value is invalid")
            setattr(self, "current_player", current_player)

        if current_player != self.current_player:
            raise Exception("current_player arg and instance mismatch.")

        if self.current_player == 'X':
            setattr(self, "current_player", "O")
        elif self.current_player == 'O':
            setattr(self, "current_player", "X")
        else:
            setattr(self, "current_player", default_next_player)

    def update_is_over(self):
        grid = getattr(self, "grid")

        # rows is the list of all rows in a grid each element is a list of 3 and there is 3 elements in total
        rows = list(partition(3, grid)) # https://toolz.readthedocs.io/en/latest/api.html?highlight=partition#toolz.itertoolz.partition
        cols = list(map(list, zip(*rows))) # same as rows but list of all cols
        diags = [[rows[x][x] for x in range(3)], [rows[2 - x][x] for x in range(3)]]
        all_lines = [*rows, *cols, *diags]

        if any(map(lambda l: len(set(l)) == 1 and "-" not in set(l), all_lines)):
            # Game is over if any line contains 3 occurence of the same symbol
            setattr(self, "is_over", True)
            setattr(self, "winner", getattr(self, "current_player"))


    game_id = db.Column('game_id', db.Integer, primary_key=True)
    winner = db.Column(db.String(1))
    is_over = db.Column(db.Boolean(), nullable=False)
    current_player = db.Column(db.String(1))  
    grid = db.Column(db.String(9))

