from app.repositories.user_repository import UserRepository
from datetime import datetime
from werkzeug.security import generate_password_hash

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def parse_date(self, date_str):
        return datetime.strptime(date_str, '%d/%m/%Y').date()

    def create_user(self, user_data):
        if 'password' not in user_data or user_data['password'] is None:
            raise ValueError("Password is required")

        user_data['date_of_birth'] = self.parse_date(user_data.get("date_of_birth"))
        user_data['password'] = generate_password_hash(user_data['password'])
        return self.user_repository.add_user(user_data)
    
    def get_by_email(self, email):
        return self.user_repository.get_by_email(email)
            
    def get_by_id(self, id):
        return self.user_repository.get_by_id(id)
    
    def delete_by_id(self, id):
        return self.user_repository.delete_by_id(id)
    
    def update_info_by_id(self, id, update_data):
        return self.user_repository.update_info_by_id(id, update_data)
