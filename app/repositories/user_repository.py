from app.utils.database import db
from app.model.auth.user import User

class UserRepository:
    def add_user(self, user_data):
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()
        return user

    def get_by_id(self, user_id):
        return db.session.query(User).get(user_id)

    def delete_by_id(self, user_id):
        user = db.session.query(User).get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    
    def get_by_email(self, email):
        return db.session.query(User).filter_by(email=email).first()
    
    def update_info_by_id(self, user_id, update_data):
        user = db.session.query(User).get(user_id)
        if user:
            for key, value in update_data.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            db.session.commit()
            return user
        return None
