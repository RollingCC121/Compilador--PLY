
# Definición de variables
variables = {}

# Evaluación de expresiones
def evaluate_expression(expr):
    if isinstance(expr, tuple):
        op, left, right = expr
        print(f"Evaluando expresión: {left} {op} {right}")
        left_val = evaluate_expression(left)
        right_val = evaluate_expression(right)
        if left_val is None or right_val is None:
            print("Error semántico: subexpresión no válida.")
            return None
        if op == '+':
            return left_val + right_val
        elif op == '-':
            return left_val - right_val
        elif op == '*':
            return left_val * right_val
        elif op == '/':
            if right_val != 0:
                return left_val / right_val
            else:
                print("Error semántico: división por cero.")
                return None
    elif isinstance(expr, str) and expr.isdigit():
        return int(expr)
    elif isinstance(expr, str):
        if expr in variables:
            return variables[expr]
        else:
            print(f"Error semántico: variable '{expr}' no definida.")
            return None
    else:
        print("Error semántico: expresión no válida.")
        return None


# Reglas semánticas
def check_semantics(ast):
    if isinstance(ast, tuple):
        if ast[0] == 'assign':
            _, var, expr = ast
            result = evaluate_expression(expr)
            if result is not None:
                variables[var] = result
        else:
            op, left, right = ast
            check_semantics(left)
            check_semantics(right)
    elif isinstance(ast, str) and ast.isdigit():
        # Si es un número, no hay problemas semánticos
        pass
    elif isinstance(ast, str):
        if ast not in variables:
            print(f"Error semántico: variable '{ast}' no definida.")
            return None
    else:
        print("Error semántico: nodo desconocido en el AST.")
        return None
