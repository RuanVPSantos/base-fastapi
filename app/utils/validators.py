import re

def validate_email(email: str) -> bool:
    """
    Valida se o e-mail fornecido é válido.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None

def validate_positive_number(value: float) -> bool:
    """
    Verifica se o número é positivo.
    """
    return value > 0

def validate_string_length(string: str, min_length: int, max_length: int) -> bool:
    """
    Verifica se o comprimento da string está dentro do intervalo permitido.
    """
    return min_length <= len(string) <= max_length
