import tkinter as tk
from repositories.user_repository import UserRepository
from services.user_service import UserService
from ui.app_wiki import app_wiki

if __name__ == "__main__":
    root = tk.Tk()
    user_repository = UserRepository()
    user_service = UserService(user_repository)
    app = app_wiki(root, user_service)
    root.mainloop()