import random
import string


class RandomUser:
    def __init__(self):
        self.email = self.generate_email()
        self.name = self.generate_name()
        self.password = self.generate_password()

    def generate_email(self):
        domains = ["gmail.com", "yahoo.com", "yandex.ru", "hotmail.com"]
        return f"{self.generate_random_string(8)}@{random.choice(domains)}"

    def generate_name(self):
        return self.generate_random_string(12)

    def generate_password(self):
        return self.generate_random_string(12)

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string


