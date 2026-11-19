class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def show_info(self):
        print(f"Пользователь: {self.username}, Email: {self.email}")
