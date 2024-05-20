from aParser.analizadorSintactico import parser  # Importa el parser desde el módulo especificado

class SemanticAnalyzer:
    def __init__(self):
        self.variables = {}  # Diccionario para almacenar las variables definidas y sus tipos

    def analyze(self, tree):
        # Recorre el árbol sintáctico y analiza cada nodo
        for node in tree:
            if node[0] == 'assign':
                # Si el nodo es una asignación, maneja la asignación
                self.handle_assignment(node[1], node[2])
            elif node[0] in ('+', '-', '*', '/', '^', 'sqrt', 'log', '<', '>', '<=', '>=', '==', '!='):
                # Si el nodo es una expresión, maneja la expresión
                self.handle_expression(node)

    def handle_assignment(self, var_name, value):
        # Maneja la asignación de una variable
        if isinstance(value, tuple):
            if value[0] == 'identifier':
                # Si el valor es un identificador, verifica si la variable está definida
                if value[1] not in self.variables:
                    # Si la variable no está definida, imprime un error semántico
                    print(f"Error semántico: La variable '{value[1]}' no está definida.")
            elif value[0] == 'number':
                # Si el valor es un número, asigna el tipo 'number' a la variable
                self.variables[var_name] = 'number'
        elif isinstance(value, tuple) and value[0] in ('+', '-', '*', '/', '^', 'sqrt', 'log', '<', '>', '<=', '>=', '==', '!='):
            # Si el valor es una expresión, maneja la expresión
            self.handle_expression(value)

    def handle_expression(self, node):
        # Maneja las expresiones
        left, right = node if len(node) == 3 else (node[0], node[1], None)  # Desempaqueta los operadores y operandos
        if isinstance(left, tuple) and left[0] == 'identifier':
            # Verifica si el operando izquierdo es una variable definida
            if left[1] not in self.variables:
                # Si la variable no está definida, imprime un error semántico
                print(f"Error semántico: La variable '{left[1]}' no está definida.")
        elif isinstance(left, tuple) and left[0] in ('+', '-', '*', '/', '^', 'sqrt', 'log', '<', '>', '<=', '>=', '==', '!='):
            # Si el operando izquierdo es otra expresión, maneja la expresión recursivamente
            self.handle_expression(left)
        if right:
            # Si hay un operando derecho, verifica si es una variable definida
            if isinstance(right, tuple) and right[0] == 'identifier':
                # Si la variable no está definida, imprime un error semántico
                if right[1] not in self.variables:
                    print(f"Error semántico: La variable '{right[1]}' no está definida.")
            elif isinstance(right, tuple) and right[0] in ('+', '-', '*', '/', '^', 'sqrt', 'log', '<', '>', '<=', '>=', '==', '!='):
                # Si el operando derecho es otra expresión, maneja la expresión recursivamente
                self.handle_expression(right)
