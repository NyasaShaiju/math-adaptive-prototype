import random

def generate_puzzle(level):
    """
    Returns a tuple (expression_str, numeric_answer).
    level: "Easy", "Medium", "Hard"
    """
    if level == "Easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(["+", "-"])
    elif level == "Medium":
        a, b = random.randint(5, 20), random.randint(5, 20)
        op = random.choice(["+", "-", "*"])
    else:  # Hard
        a, b = random.randint(10, 50), random.randint(1, 10)
        op = random.choice(["+", "-", "*", "/"])
        if op == "/":
            b = random.randint(1, 10)
            a = b * random.randint(2, 10)

    expr = f"{a} {op} {b}"
    answer = eval(expr)
    return expr, answer
