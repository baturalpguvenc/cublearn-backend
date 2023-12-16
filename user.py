class User:
    def __init__(self, wallet, name, surname, email, is_admin=False):
        self.wallet = wallet
        self.name = name
        self.surname = surname
        self.email = email
        self.is_admin = is_admin  

    def update_info(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def set_admin(self, is_admin):
        self.is_admin = is_admin