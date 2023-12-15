class User:
    def __init__(self, wallet, name, surname, email, is_admin=False):
        # Kullanıcı nesnesini oluştururken gerekli bilgileri alır
        self.wallet = wallet
        self.name = name
        self.surname = surname
        self.email = email
        self.is_admin = is_admin  # Admin yetkisi eklenmiştir

    def update_info(self, name, surname, email):
        # Kullanıcının bilgilerini güncelleme
        self.name = name
        self.surname = surname
        self.email = email

    def set_admin(self, is_admin):
        # Admin yetkisini ayarlama
        self.is_admin = is_admin