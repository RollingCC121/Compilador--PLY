MOV_REG_CONST = 0x10  # Mueve un valor constante a un registro
ADD_REG_REG = 0x20    # Suma el valor de dos registros
MUL_REG_REG = 0x30    # Multiplica el valor de dos registros
MOV_REG_REG = 0x40    # Mueve el valor de un registro a otro

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
        # Busca un registro disponible que no esté en uso
        for reg, val in registers.items():
            if reg not in self.used_registers:
                self.used_registers.add(reg)
                variable_registers[variable] = reg
                return val
        # Si no se encuentra ningún registro disponible, libera uno de los registros en uso
        if self.used_registers:
            released_register = self.used_registers.pop()
            del variable_registers[next(iter(variable_registers))]  # Elimina la primera variable asignada
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
        return len(tokens) == 5 and tokens[1] == '=' and tokens[3] in ('+', '*')

    def generate_assignment_constant(self, tokens):
        # Asignación de constante
        dest_register = self.get_register(tokens[0])
        if isinstance(dest_register, int):
            self.binary_code.append(0b00000001)  # MOV_REG_CONST
            self.binary_code.append(dest_register)
            self.binary_code.append(int(tokens[2]))
        else:
            raise Exception("No hay más registros disponibles")
        


    def generate_assignment_variable(self, tokens):
        # Asignación de una variable a otra
        self.binary_code.append(MOV_REG_REG)
        self.binary_code.append(self.get_register(tokens[0]))
        self.binary_code.append(self.get_register(tokens[2]))

    def handle_operation(self, tokens):
        # Obtener registros para las variables involucradas en la operación
        dest = self.get_register(tokens[0])
        src1 = self.get_register(tokens[2])
        op = tokens[3]
        src2 = self.get_register(tokens[4])

        # Realizar la operación y almacenar el resultado en el registro de destino
        if op == '+':
            self.binary_code.append(ADD_REG_REG)
        elif op == '*':
            self.binary_code.append(MUL_REG_REG)
        
        self.binary_code.append(dest)
        self.binary_code.append(src1)
        self.binary_code.append(src2)

        # Liberar registros temporales después de su uso
        if 'temp' in tokens[2]:
            self.release_register(tokens[2])
        if 'temp' in tokens[4]:
            self.release_register(tokens[4])
    
    def release_register(self, variable):
        # Libera el registro asociado con la variable
        if variable in variable_registers:
            reg = variable_registers[variable]
            del variable_registers[variable]
            self.used_registers.remove(reg)

    def get_binary_code(self):
        return self.binary_code
