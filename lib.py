def calculate_factorial(n: int) -> int:
    """
    Обчислює факторіал числа рекурсивним методом.
    Приймає ціле невід'ємне число.
    """
    if n < 0:
        raise ValueError("Факторіал визначений лише для невід'ємних чисел.")
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

def greet_user(name: str) -> str:
    """
    Формує персоналізоване привітання для користувача.
    """
    return f"Привіт, {name}! Успішного виконання лабораторної."