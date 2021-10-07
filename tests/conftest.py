import pytest

from app import create_app
from app.extensions import db


@pytest.fixture(scope='module')
def app():
    app = create_app()

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
        db.session.commit()

