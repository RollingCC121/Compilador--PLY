from aParser.analizadorSintactico import parser

class IntermediateCodeGenerator:
    def __init__(self):
        self.intermediate_code = []
        self.temp_counter = 0

    def generate_code(self, tree):
        for node in tree:
            if node[0] == 'assign':
                self.generate_assignment_code(node[1], node[2])
            elif node[0] in ('+', '-', '*', '/'):
                temp_var = f'temp{self.temp_counter}'
                self.temp_counter += 1
                self.generate_expression_code(node, temp_var)

    def generate_assignment_code(self, var_name, value):
        if isinstance(value, int):
            self.intermediate_code.append(f'{var_name} = {value}')
        elif isinstance(value, tuple):
            if value[0] == 'number':
                self.intermediate_code.append(f'{var_name} = {value[1]}')
            elif value[0] == 'identifier':
                self.intermediate_code.append(f'{var_name} = {value[1]}')
            elif value[0] in ('+', '-', '*', '/'):
                temp_var = f'temp{self.temp_counter}'
                self.temp_counter += 1
                self.generate_expression_code(value, temp_var)
                self.intermediate_code.append(f'{var_name} = {temp_var}')

    def generate_expression_code(self, node, result_var):
        op, left, right = node
        if isinstance(left, tuple) and left[0] == 'identifier':
            left_operand = left[1]
        elif isinstance(left, tuple):
            left_operand = f'temp{self.temp_counter}'
            self.temp_counter += 1
            self.generate_expression_code(left, left_operand)
        else:
            left_operand = left

        if isinstance(right, tuple) and right[0] == 'identifier':
            right_operand = right[1]
        elif isinstance(right, tuple):
            right_operand = f'temp{self.temp_counter}'
            self.temp_counter += 1
            self.generate_expression_code(right, right_operand)
        else:
            right_operand = right

        self.intermediate_code.append(f'{result_var} = {left_operand} {op} {right_operand}')


class CodeOptimizer:
    def __init__(self):
        pass

    def optimize_code(self, intermediate_code):
        optimized_code = []
        assignments = set()
        
        for line in intermediate_code:
            tokens = line.split(' ')
            if len(tokens) >= 3 and tokens[1] == '=':
                target = tokens[0]
                if target not in assignments:
                    assignments.add(target)
                    optimized_code.append(line)
            else:
                optimized_code.append(line)
        
        return optimized_code

'''
# Ejemplo de uso
data = """
x = 5
y = 10
z = x + y * 2"""

# Análisis sintáctico
result = parser.parse(data)

# Generador de código intermedio
code_generator = IntermediateCodeGenerator()
code_generator.generate_code(result)


# Imprimir código intermedio generado antes de la optimización
print("Código Intermedio (Antes de la Optimización):")
for line in code_generator.intermediate_code:
    print(line)


# Optimización de código
optimizer = CodeOptimizer()
optimized_code = optimizer.optimize_code(code_generator.intermediate_code)

# Imprimir código intermedio optimizado
print("\nCódigo Intermedio Optimizado:")
for line in optimized_code:
    print(line)
'''