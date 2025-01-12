import json
import os

class User:
    """
    Kullanıcıyı temsil eden sınıf.

    Attributes:
        username (str): Kullanıcının kullanıcı adı.
        password (str): Kullanıcının şifresi.
        email (str): Kullanıcının e-posta adresi.
    """
    def __init__(self, username, password, email):
        """
        Kullanıcı sınıfını başlatır.

        Args:
            username (str): Kullanıcının kullanıcı adı.
            password (str): Kullanıcının şifresi.
            email (str): Kullanıcının e-posta adresi.
        """
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    """
    Kullanıcı kayıtları ve giriş/çıkış işlemlerini yöneten sınıf.

    Attributes:
        users (list): Sistemde kayıtlı tüm kullanıcıların listesi.
        isLoggedIn (bool): Kullanıcının giriş yapıp yapmadığını kontrol eder.
        currentUser (User): Giriş yapan mevcut kullanıcı bilgisi.
    """

    def __init__(self):
        """
        UserRepository sınıfını başlatır ve kullanıcı listesini yükler.
        """
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # JSON dosyasından kullanıcıları yükle
        self.loadUsers()

    def loadUsers(self):
        """
        JSON dosyasından kullanıcıları yükler ve kullanıcı listesine ekler.
        """
        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user['username'], password=user['password'], email=user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user: User):
        """
        Yeni bir kullanıcı kaydeder.

        Args:
            user (User): Kaydedilecek kullanıcı nesnesi.
        """
        self.users.append(user)
        self.savetoFile()
        print('Kullanıcı oluşturuldu.')

    def login(self, username, password):
        """
        Kullanıcının giriş yapmasını sağlar.

        Args:
            username (str): Kullanıcının kullanıcı adı.
            password (str): Kullanıcının şifresi.

        Not:
            Kullanıcı adı ve şifre eşleşirse giriş başarılı olur.
        """
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('login yapıldı.')
                break

    def logout(self):
        """
        Kullanıcının çıkış yapmasını sağlar.
        """
        self.isLoggedIn = False
        self.currentUser = {}
        print('Çıkış yapıldı.')

    def identity(self):
        """
        Giriş yapan kullanıcının bilgilerini ekrana yazdırır.
        """
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('giriş yapılmadı.')

    def savetoFile(self):
        """
        Kullanıcı listesini JSON dosyasına kaydeder.
        """
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open('users.json', 'w') as file:
            json.dump(list, file)


# Kullanıcı kayıtlarını yöneten nesne
repository = UserRepository()

while True:
    """
    Kullanıcı etkileşim menüsü:
        1- Kullanıcı kaydı yapma.
        2- Giriş yapma.
        3- Çıkış yapma.
        4- Giriş yapan kullanıcı bilgilerini görme.
        5- Çıkış (programdan).
    """
    print('Menü'.center(50, '*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- identity\n5- Exit\nseçiminiz: ')
    if secim == '5':
        break
    else:
        if secim == '1':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            user = User(username=username, password=password, email=email)
            repository.register(user)
        elif secim == '2':
            if repository.isLoggedIn:
                print('zaten login oldunuz')
            else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username, password)
        elif secim == '3':
            repository.logout()
        elif secim == '4':
            repository.identity()
        else:
            print('yanlış seçim')
