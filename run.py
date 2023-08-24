from app import auth
from app import admin
from app import app
from db import db

app.register_blueprint(auth.auth)
app.register_blueprint(admin.admin, url_prefix='/admin')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8000)
