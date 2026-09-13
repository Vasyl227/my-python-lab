# Моя лабораторна робота з Python

## UML Діаграма компонентів
```mermaid
classDiagram
    class main {
        +main()
    }
    class lib {
        +calculate_factorial(n: int) int
        +greet_user(name: str) str
    }
    main ..> lib : imports