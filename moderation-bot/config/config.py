# config.py

import json

class Config:
    def __init__(self):
        self.load_permissions()

    def load_permissions(self):
        with open('permissions.json', 'r') as file:
            self.permissions = json.load(file)

    def save_permissions(self):
        with open('permissions.json', 'w') as file:
            json.dump(self.permissions, file, indent=4)

    def get_permission(self, role):
        return self.permissions.get(role, [])

    def set_permission(self, role, permissions):
        self.permissions[role] = permissions
        self.save_permissions()

    def remove_permission(self, role):
        if role in self.permissions:
            del self.permissions[role]
            self.save_permissions()

# End of config.py