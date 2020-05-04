from .app import app
from .routes import shortener


app.register_blueprint(shortener)


if __name__ == '__main__':
    app.run()
