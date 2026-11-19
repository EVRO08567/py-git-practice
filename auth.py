class Auth:
    def login(self, user, password):
        if user.username and password:
            print(f"Пользователь {user.username} вошел в систему.")
            return True
        return False
