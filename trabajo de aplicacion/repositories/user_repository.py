from models.user import User
from uuid import UUID


class UserRepository:
    def find_all(self) -> list[User]:
        return self.users
    
    def __init__(self):
        self.users: list[User] = []


    def create_one(self, user: User):
        self.users.append(user)

    def delete_one(self, user_uuid: UUID):
        self.users = [user for user in self.users if user.uuid != user_uuid]

    def update_user(self, user_uuid: UUID, fname: str, lname: str, age: int, email: str):
        users = [user for user in self.users if user.uuid == user_uuid]
        if users:
            user = users[0]
            user.fname = fname
            user.lname = lname
            user.email = email
            user.age = age