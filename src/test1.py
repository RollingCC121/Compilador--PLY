from analizadorSintactico import parser

def semantic_analysis(tree, symbol_table):
    for node in tree:
        if node[0] == 'assign':
            variable_name = node[1]
            expression = node[2]
            value = eval_expression(expression, symbol_table)
            # Verificar la asignación de tipos
            if variable_name in symbol_table:
                expected_type = symbol_table[variable_name]['type']
                if not isinstance(value, expected_type):
                    raise ValueError(f"Error de tipo: se esperaba {expected_type} para '{variable_name}'")
            symbol_table[variable_name] = {'value': value, 'type': type(value)}
        elif isinstance(node, tuple):
            semantic_analysis(node, symbol_table)

def eval_expression(expression, symbol_table):
    if isinstance(expression, tuple):
        op, left, right = expression
        left_value = eval_expression(left, symbol_table)
        right_value = eval_expression(right, symbol_table)
        # Verificar la operación
        if op in ('+', '-', '*', '/'):
            # Verificar la compatibilidad de tipos para operaciones aritméticas
            if not (isinstance(left_value, int) and isinstance(right_value, int)):
                raise ValueError("Error de tipo: se esperaban operandos numéricos para la operación aritmética")
            if op == '/' and right_value == 0:
                raise ValueError("Error: división por cero")
            return eval(f"left_value {op} right_value")
    elif isinstance(expression, str):
        # Verificar el uso adecuado de variables
        if expression not in symbol_table:
            raise ValueError(f"Error: variable '{expression}' no definida")
        return symbol_table[expression]['value']
    else:
        return expression

# Ejemplo de uso
input_code = """
x = 5
y = 10
z = x + y * 2
"""

symbol_table = {}
parsed_tree = parser.parse(input_code)
semantic_analysis(parsed_tree, symbol_table)
