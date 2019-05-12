import os

from web import create_app

app = create_app(os.environ.get('FLASK_ENV'))

if __name__ == '__main__':
    app.run(host="0.0.0.0")
