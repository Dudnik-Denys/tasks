def verification(login: str, password: str, success: callable, failure: callable) -> callable:
    if not isinstance(password, str):
        return failure(login, 'в пароле нет ни одной буквы')
    if len([char for char in password if ord(char) in range(65, 91) or ord(char) in range(97, 123)]) < 1:
        return failure(login, 'в пароле нет ни одной буквы')
    if len([char for char in password if ord(char) in range(65, 91)]) < 1:
        return failure(login, 'в пароле нет ни одной заглавной буквы')
    if len([char for char in password if ord(char) in range(97, 123)]) < 1:
        return failure(login, 'в пароле нет ни одной строчной буквы')
    if len([char for char in password if char.isdigit()]) < 1:
        return failure(login, 'в пароле нет ни одной цифры')
    return success(login)
