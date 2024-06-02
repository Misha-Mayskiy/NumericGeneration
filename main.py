import random
import sympy as sp


# Функция для генерации числового примера
# Функция для генерации числового примера
def generate_numerical(level):
    operations = ['+', '-', '*', '/']
    if level == 'легкий':
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
    elif level == 'средний':
        num1, num2 = random.randint(10, 50), random.randint(10, 50)
    else:  # сложный
        num1, num2 = random.randint(50, 100), random.randint(50, 100)
    operation = random.choice(operations)
    question = f"{num1} {operation} {num2}"

    # Обработка операции деления
    if operation == '/':
        # Проверка на целочисленное деление
        if num1 % num2 == 0:
            answer = num1 // num2
        else:
            # Округление до двух знаков после запятой
            answer = round(num1 / num2, 2)
    else:
        answer = eval(question)

    return question, answer


# Функция для генерации уравнения с одной переменной
def generate_equation(level):
    if level == 'легкий':
        num = random.randint(1, 10)
        result = random.randint(1, 20)
        return f"x + {num} = {result}", result - num
    elif level == 'средний':
        num = random.randint(2, 5)
        result = random.randint(10, 50)
        return f"x * {num} = {result}", result / num
    else:  # сложный
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        # Решение квадратного уравнения через дискриминант
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            x1 = sp.Rational(-b + sp.sqrt(discriminant), 2 * a)
            x2 = sp.Rational(-b - sp.sqrt(discriminant), 2 * a)
            return f"{a}x^2 + {b}x + {c} = 0", (x1, x2)
        elif discriminant == 0:
            x = sp.Rational(-b, 2 * a)
            return f"{a}x^2 + {b}x + {c} = 0", x
        else:
            return f"{a}x^2 + {b}x + {c} = 0", "нет реальных корней"


# Функция для генерации неравенства с одной переменной
def generate_inequality(level):
    signs = ['<', '>', '<=', '>=']
    if level == 'легкий':
        num = random.randint(1, 10)
        result = random.randint(1, 20)
        sign = random.choice(signs)
        return f"x + {num} {sign} {result}", f"x {sign} {result - num}"
    elif level == 'средний':
        num = random.randint(2, 5)
        result = random.randint(10, 50)
        sign = random.choice(signs)
        return f"x * {num} {sign} {result}", f"x {sign} {result // num}"
    else:  # сложный
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        sign = random.choice(['<', '>', '<=', '>='])
        # Решение квадратного неравенства через дискриминант
        discriminant = b ** 2 - 4 * a * c
        if discriminant >= 0:
            x1 = sp.Rational(-b + sp.sqrt(discriminant), 2 * a)
            x2 = sp.Rational(-b - sp.sqrt(discriminant), 2 * a)
            if a > 0:
                if sign in ['>', '>=']:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", f"x < {x1} или x > {x2}"
                else:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", f"{x1} < x < {x2}"
            else:
                if sign in ['>', '>=']:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", "нет решения"
                else:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", "все x"
        else:
            if a > 0:
                if sign in ['>', '>=']:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", "все x"
                else:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", "нет решения"
            else:
                if sign in ['>', '>=']:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", "нет решения"
                else:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", "все x"


# Главная функция для выбора типа и сложности примера
def generate_example(difficulty=None, example_type=None):
    if not difficulty:
        difficulty = random.choice(['легкий', 'средний', 'сложный'])
    if not example_type:
        example_type = random.choice(['числовые примеры', 'уравнения', 'неравенства'])

    if example_type == 'числовые примеры':
        question, answer = generate_numerical(difficulty)
    elif example_type == 'уравнения':
        question, answer = generate_equation(difficulty)
    else:  # неравенства
        question, answer = generate_inequality(difficulty)

    return question, answer


# Функция для проверки ответа пользователя
def check_answer(user_answer, correct_answer):
    print(str(correct_answer))
    if str(correct_answer) == user_answer.strip():
        return "Правильно!"
    else:
        return f"Неправильно. Правильный ответ: {correct_answer}"


if __name__ == "__main__":
    difficulty = input("Выберите сложность (легкий, средний, сложный): ")
    example_type = input("Выберите тип примера (числовые примеры, уравнения, неравенства): ")
    question, correct_answer = generate_example(difficulty, example_type)
    print(f"Ваш пример: {question}")
    user_answer = input("Введите ваш ответ: ")
    print(check_answer(user_answer, correct_answer))
