from flask_jwt_extended import JWTManager

def init_jwt(app):
    app.config['JWT_SECRET_KEY'] = 's2+0yPEqnCMaOs8XQVHveMMB+/ZunTKE/4m4oj/XlAo='
    jwt = JWTManager(app)
