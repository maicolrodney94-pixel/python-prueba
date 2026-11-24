from uuid import UUID
from models.user import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self) -> list[User]:
        return self.user_repository.find_all()

    def create_user(self, fname: str, lname: str, age: int, email: str):
        if not fname.strip() or not lname.strip() or age <= 0 or not email.strip():
            raise ValueError("todos los campos son obligatorios y deben ser válidos")
        new_user = User(fname=fname.strip(), lname=lname.strip(), age=age, email=email.strip())
        self.user_repository.create_one(new_user)

    def delete_user(self, user_uuid: UUID):
        self.user_repository.delete_one(user_uuid)

    def update_user(self, user_uuid: UUID, fname: str, lname: str, age: int, email: str):
        self.user_repository.update_user(user_uuid, fname, lname, age, email)
