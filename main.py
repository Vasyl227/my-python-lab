from lib import calculate_factorial, greet_user

def main():
    """
    Головний метод, який імпортує функції з модуля lib, 
    передає їм параметри та виводить результат у консоль.
    """
    # Виклик функції привітання
    greeting = greet_user("Студент")
    print(greeting)

    # Виклик математичної функції
    number = 5
    result = calculate_factorial(number)
    print(f"Факторіал числа {number} дорівнює {result}.")

if __name__ == "__main__":
    main()