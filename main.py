import re

# Проверки пароля на соответствие требованиям
def is_valid_password(password):
    # Длину пароля
    if len(password) < 8:
        return False

    # Содержание прописных
    if not re.search(r'[A-Z]', password):
        return False

    # Содержание строчных
    if not re.search(r'[a-z]', password):
        return False

    # Содержание цифр
    if not re.search(r'\d', password):
        return False

    # Содержание спец символов
    if not re.search(r'[!@#$%^&*]', password):
        return False

    return True

# Чтение файла
with open('password.txt', 'r') as file:
    passwords = file.read().splitlines()

# Проверка паролдя и вывод
valid_passwords = [password for password in passwords if is_valid_password(password)]

# Ввод удовлетворяющих паролей
print("Допустимые пароли:")
for password in valid_passwords:
    print(password)