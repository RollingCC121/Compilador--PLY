from aParser.analizadorSintactico import parser

class IntermediateCodeGenerator:
    def __init__(self):
        self.intermediate_code = []
        self.temp_counter = 0

    def generate_code(self, tree):
        for node in tree:
            if node[0] == 'assign':
                self.generate_assignment_code(node[1], node[2])

    def handle_expression(self, node):
        if isinstance(node, int):
            return str(node)
        elif isinstance(node, tuple):
            if node[0] == 'number':
                return str(node[1])
            elif node[0] == 'identifier':
                return node[1]
            elif node[0] in ('+', '-', '*', '/', '^'):
                left = self.handle_expression(node[1])
                right = self.handle_expression(node[2])
                temp_var = f'temp{self.temp_counter}'
                self.temp_counter += 1
                self.intermediate_code.append(f'{temp_var} = {left} {node[0]} {right}')
                return temp_var
            elif node[0] == 'sqrt':
                operand = self.handle_expression(node[1])
                temp_var = f'temp{self.temp_counter}'
                self.temp_counter += 1
                self.intermediate_code.append(f'{temp_var} = sqrt({operand})')
                return temp_var
            elif node[0] == 'log':
                operand = self.handle_expression(node[1])
                temp_var = f'temp{self.temp_counter}'
                self.temp_counter += 1
                self.intermediate_code.append(f'{temp_var} = log({operand})')
                return temp_var
            elif node[0] in ('<', '>', '<=', '>=', '==', '!='):
                left = self.handle_expression(node[1])
                right = self.handle_expression(node[2])
                temp_var = f'temp{self.temp_counter}'
                self.temp_counter += 1
                self.intermediate_code.append(f'{temp_var} = {left} {node[0]} {right}')
                return temp_var
        else:
            return str(node)

    def generate_assignment_code(self, var_name, value):
        if isinstance(value, int):
            self.intermediate_code.append(f'{var_name} = {value}')
        elif isinstance(value, tuple):
            result = self.handle_expression(value)
            self.intermediate_code.append(f'{var_name} = {result}')

    def generate_expression_code(self, node, result_var):
        op = node[0]
        if op in ('+', '-', '*', '/', '^', '<', '>', '<=', '>=', '==', '!='):
            left = node[1]
            right = node[2]
            left_operand = self.handle_expression(left)
            right_operand = self.handle_expression(right)
            self.intermediate_code.append(f'{result_var} = {left_operand} {op} {right_operand}')
        elif op in ('sqrt', 'log'):
            operand = self.handle_expression(node[1])
            self.intermediate_code.append(f'{result_var} = {op}({operand})')

    def print_code(self):
        for line in self.intermediate_code:
            print(line)



