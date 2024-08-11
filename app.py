from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env.example file.

from app import app, db
from flask_migrate import Migrate

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(debug=True)
