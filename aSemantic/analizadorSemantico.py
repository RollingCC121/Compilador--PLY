from aParser.analizadorSintactico import parser

class SemanticAnalyzer:
    def __init__(self):
        self.variables = {}

    def analyze(self, tree):
        for node in tree:
            if node[0] == 'assign':
                if self.handle_assignment(node[1], node[2]):
                    print(f"Asignación de '{node[1]}' correcta.")
            elif node[0] in ('+', '-', '*', '/'):
                if self.handle_expression(node):
                    print("Expresión analizada correctamente.")

    def handle_assignment(self, var_name, value):
        if isinstance(value, tuple):
            if value[0] == 'identifier':
                if value[1] not in self.variables:
                    print(f"Error semántico: La variable '{value[1]}' no está definida.")
                    return False
            elif value[0] == 'number':
                self.variables[var_name] = 'number'
        elif isinstance(value, tuple) and value[0] in ('+', '-', '*', '/'):
            self.handle_expression(value)
        return True

    def handle_expression(self, node):
        op, left, right = node
        if isinstance(left, tuple) and left[0] == 'identifier':
            if left[1] not in self.variables:
                print(f"Error semántico: La variable '{left[1]}' no está definida.")
                return False
        elif isinstance(left, tuple) and left[0] in ('+', '-', '*', '/'):
            self.handle_expression(left)
        if isinstance(right, tuple) and right[0] == 'identifier':
            if right[1] not in self.variables:
                print(f"Error semántico: La variable '{right[1]}' no está definida.")
                return False
        elif isinstance(right, tuple) and right[0] in ('+', '-', '*', '/'):
            self.handle_expression(right)
        return True
'''
# Ejemplo de uso
data = """
x = 5
y = 10
z = x + y * 2"""
result = parser.parse(data)

# Analizador semántico
semantic_analyzer = SemanticAnalyzer()
semantic_analyzer.analyze(result)
'''