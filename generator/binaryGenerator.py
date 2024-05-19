MOV_REG_CONST = 0x10  # Mueve un valor constante a un registro
ADD_REG_REG = 0x20    # Suma el valor de dos registros
SUB_REG_REG = 0x50    # Resta el valor de dos registros
MUL_REG_REG = 0x30    # Multiplica el valor de dos registros
DIV_REG_REG = 0x40    # Divide el valor de dos registros
MOV_REG_REG = 0x40    # Mueve el valor de un registro a otro
SQRT_REG = 0x60       # Instrucción para raíz cuadrada
LOG_REG = 0x70        # Instrucción para logaritmo
POW_REG_REG = 0x80    # Instrucción para potencia
CMP_REG_REG = 0x90    # Instrucción para comparar dos registros

registers = {
    'R0': 0x00,
    'R1': 0x01,
    'R2': 0x02,
    'R3': 0x03,
    'R4': 0x04,
    'R5': 0x05,
    'R6': 0x06,
    'R7': 0x07,
}

variable_registers = {}

class BinaryCodeGenerator:
    def __init__(self):
        self.binary_code = bytearray()
        self.used_registers = set()

    def get_register(self, variable):
        for reg, val in registers.items():
            if reg not in self.used_registers:
                self.used_registers.add(reg)
                variable_registers[variable] = reg
                return val
        if self.used_registers:
            released_register = self.used_registers.pop()
            del variable_registers[next(iter(variable_registers))]
            variable_registers[variable] = released_register
            return registers[released_register]
        raise Exception("No hay más registros disponibles")
    
    def validate_and_generate_code(self, intermediate_code):
        for line in intermediate_code:
            tokens = line.split()
            if self.is_valid_assignment_constant(tokens):
                self.generate_assignment_constant(tokens)
            elif self.is_valid_assignment_variable(tokens):
                self.generate_assignment_variable(tokens)
            elif self.is_valid_operation(tokens):
                self.handle_operation(tokens)
            else:
                print(f"Formato desconocido de línea de código intermedio: {line}")
                raise ValueError(f"Formato incorrecto en línea: {line}")

    def is_valid_assignment_constant(self, tokens):
        return len(tokens) == 3 and tokens[1] == '=' and tokens[2].isdigit()

    def is_valid_assignment_variable(self, tokens):
        return len(tokens) == 3 and tokens[1] == '=' and not tokens[2].isdigit()

    def is_valid_operation(self, tokens):
        if len(tokens) == 5 and tokens[1] == '=' and tokens[3] in ('+', '*', '-', '/', '^', '<', '<=', '>', '>=', '==', '!='):
            return True
        if len(tokens) == 4 and tokens[1] == '=' and tokens[2] in ('sqrt', 'log'):
            return True
        return False

    def generate_assignment_constant(self, tokens):
        dest_register = self.get_register(tokens[0])
        if isinstance(dest_register, int):
            self.binary_code.append(MOV_REG_CONST)
            self.binary_code.append(dest_register)
            self.binary_code.append(int(tokens[2]))
        else:
            raise Exception("No hay más registros disponibles")

    def generate_assignment_variable(self, tokens):
        self.binary_code.append(MOV_REG_REG)
        self.binary_code.append(self.get_register(tokens[0]))
        self.binary_code.append(self.get_register(tokens[2]))

    def handle_operation(self, tokens):
        dest = self.get_register(tokens[0])
        op = tokens[2] if len(tokens) == 4 else tokens[3]
        
        if op in ('+', '-', '*', '/', '^'):
            src1 = self.get_register(tokens[2])
            src2 = self.get_register(tokens[4])
            if op == '+':
                self.binary_code.append(ADD_REG_REG)
            elif op == '-':
                self.binary_code.append(SUB_REG_REG)
            elif op == '*':
                self.binary_code.append(MUL_REG_REG)
            elif op == '/':
                self.binary_code.append(DIV_REG_REG)
            elif op == '^':
                self.binary_code.append(POW_REG_REG)
            
            self.binary_code.append(dest)
            self.binary_code.append(src1)
            self.binary_code.append(src2)
            
            if 'temp' in tokens[2]:
                self.release_register(tokens[2])
            if 'temp' in tokens[4]:
                self.release_register(tokens[4])
        
        elif op in ('<', '<=', '>', '>=', '==', '!='):
            src1 = self.get_register(tokens[2])
            src2 = self.get_register(tokens[4])
            self.binary_code.append(CMP_REG_REG)
            self.binary_code.append(dest)
            self.binary_code.append(src1)
            self.binary_code.append(src2)
            
            if 'temp' in tokens[2]:
                self.release_register(tokens[2])
            if 'temp' in tokens[4]:
                self.release_register(tokens[4])
        
        elif op == 'sqrt':
            src = self.get_register(tokens[3])
            self.binary_code.append(SQRT_REG)
            self.binary_code.append(dest)
            self.binary_code.append(src)
            
            if 'temp' in tokens[3]:
                self.release_register(tokens[3])
        
        elif op == 'log':
            src = self.get_register(tokens[3])
            self.binary_code.append(LOG_REG)
            self.binary_code.append(dest)
            self.binary_code.append(src)
            
            if 'temp' in tokens[3]:
                self.release_register(tokens[3])

    def release_register(self, variable):
        if variable in variable_registers:
            reg = variable_registers[variable]
            del variable_registers[variable]
            self.used_registers.remove(reg)

    def get_binary_code(self):
        return self.binary_code
