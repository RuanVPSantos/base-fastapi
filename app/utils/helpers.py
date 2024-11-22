from datetime import datetime

def format_date(date: datetime, format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Formata uma data para uma string no formato especificado.
    """
    return date.strftime(format)

def calculate_percentage(part: float, total: float) -> float:
    """
    Calcula a porcentagem de uma parte em relação ao total.
    """
    if total == 0:
        return 0
    return (part / total) * 100
