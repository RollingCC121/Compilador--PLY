from aParser.analizadorSintactico import parser  # Importa el parser desde el módulo especificado

class IntermediateCodeGenerator:
    def __init__(self):
        # Inicializa la lista para almacenar el código intermedio generado
        self.intermediate_code = []
        # Inicializa el contador para las variables temporales
        self.temp_counter = 0

    def generate_code(self, tree):
        # Recorre el árbol sintáctico y genera el código intermedio para cada nodo
        for node in tree:
            if node[0] == 'assign':
                # Si el nodo es una asignación, genera el código intermedio para la asignación
                self.generate_assignment_code(node[1], node[2])

    def handle_expression(self, node):
        # Maneja la generación de código intermedio para las expresiones
        if isinstance(node, int):
            # Si el nodo es un entero, retorna su representación como cadena
            return str(node)
        elif isinstance(node, tuple):
            if node[0] == 'number':
                # Si el nodo es un número, retorna su valor como cadena
                return str(node[1])
            elif node[0] == 'identifier':
                # Si el nodo es un identificador, retorna el nombre del identificador
                return node[1]
            elif node[0] in ('+', '-', '*', '/', '^'):
                # Si el nodo es una operación aritmética, maneja la operación
                left = self.handle_expression(node[1])
                right = self.handle_expression(node[2])
                temp_var = f'temp{self.temp_counter}'  # Genera una variable temporal
                self.temp_counter += 1  # Incrementa el contador de variables temporales
                # Añade la operación al código intermedio
                self.intermediate_code.append(f'{temp_var} = {left} {node[0]} {right}')
                return temp_var
            elif node[0] == 'sqrt':
                # Si el nodo es una operación de raíz cuadrada, maneja la operación
                operand = self.handle_expression(node[1])
                temp_var = f'temp{self.temp_counter}'  # Genera una variable temporal
                self.temp_counter += 1  # Incrementa el contador de variables temporales
                # Añade la operación al código intermedio
                self.intermediate_code.append(f'{temp_var} = sqrt({operand})')
                return temp_var
            elif node[0] == 'log':
                # Si el nodo es una operación de logaritmo, maneja la operación
                operand = self.handle_expression(node[1])
                temp_var = f'temp{self.temp_counter}'  # Genera una variable temporal
                self.temp_counter += 1  # Incrementa el contador de variables temporales
                # Añade la operación al código intermedio
                self.intermediate_code.append(f'{temp_var} = log({operand})')
                return temp_var
            elif node[0] in ('<', '>', '<=', '>=', '==', '!='):
                # Si el nodo es una operación de comparación, maneja la operación
                left = self.handle_expression(node[1])
                right = self.handle_expression(node[2])
                temp_var = f'temp{self.temp_counter}'  # Genera una variable temporal
                self.temp_counter += 1  # Incrementa el contador de variables temporales
                # Añade la operación al código intermedio
                self.intermediate_code.append(f'{temp_var} = {left} {node[0]} {right}')
                return temp_var
        else:
            # Si el nodo no es una tupla, retorna su representación como cadena
            return str(node)

    def generate_assignment_code(self, var_name, value):
        # Genera el código intermedio para una asignación
        if isinstance(value, int):
            # Si el valor de la asignación es un entero, añade una línea de código intermedio correspondiente a la asignación
            self.intermediate_code.append(f'{var_name} = {value}')
        elif isinstance(value, tuple):
            # Si el valor de la asignación es una tupla (expresión), maneja la expresión
            result = self.handle_expression(value)
            # Añade la asignación del resultado al código intermedio
            self.intermediate_code.append(f'{var_name} = {result}')

    def generate_expression_code(self, node, result_var):
        # Genera el código intermedio para una expresión, almacenando el resultado en result_var
        op = node[0]  # Obtiene el operador de la expresión
        if op in ('+', '-', '*', '/', '^', '<', '>', '<=', '>=', '==', '!='):
            # Si el operador es una operación aritmética comparación, maneja la operación
            left = node[1]
            right = node[2]
            left_operand = self.handle_expression(left)  # Maneja el operando izquierdo
            right_operand = self.handle_expression(right)  # Maneja el operando derecho
            # Añade la operación al código intermedio
            self.intermediate_code.append(f'{result_var} = {left_operand} {op} {right_operand}')
        elif op in ('sqrt', 'log'):
            # Si el operador es una operación de raíz cuadrada o logaritmo, maneja la operación
            operand = self.handle_expression(node[1])  # Maneja el operando
            # Añade la operación al código intermedio
            self.intermediate_code.append(f'{result_var} = {op}({operand})')

    def print_code(self):
        # Imprime el código intermedio generado
        for line in self.intermediate_code:
            print(line)
