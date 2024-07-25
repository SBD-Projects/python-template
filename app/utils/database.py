from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = None

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 's2+0yPEqnCMaOs8XQVHveMMB+/ZunTKE/4m4oj/XlAo='
    db.init_app(app)
    global migrate
    migrate = Migrate(app, db)
