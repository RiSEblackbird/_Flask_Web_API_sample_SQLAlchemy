from flask import Flask

from database import init_db


def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config.Config')

  init_db(app)

  return app

app = create_app()