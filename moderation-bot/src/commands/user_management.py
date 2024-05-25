# user_management.py

class UserManagement:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, username):
        if user_id not in self.users:
            self.users[user_id] = username
            return True
        else:
            return False

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        else:
            return False

    def get_user(self, user_id):
        return self.users.get(user_id, None)

    def list_users(self):
        return self.users

# End of user_management.py