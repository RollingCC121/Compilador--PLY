from aParser.analizadorSintactico import parser  # Importa el parser desde el módulo analizadorSintactico

# Definición de códigos de operación para las instrucciones de la máquina
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

# Diccionario de registros con su valor correspondiente
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

# Diccionario para almacenar las variables y los registros asignados
variable_registers = {}

# Clase para generar código binario
class BinaryCodeGenerator:
    def __init__(self):
        self.binary_code = bytearray()  # Inicializa el código binario como un array de bytes
        self.used_registers = set()     # Conjunto de registros utilizados

    def get_register(self, variable):
        # Asigna un registro a una variable
        for reg, val in registers.items():
            if reg not in self.used_registers:
                self.used_registers.add(reg)  # Marca el registro como usado
                variable_registers[variable] = reg  # Asocia el registro a la variable
                return val  # Retorna el valor del registro
        if self.used_registers:
            released_register = self.used_registers.pop()  # Libera un registro si todos están ocupados
            del variable_registers[next(iter(variable_registers))]  # Elimina la variable que estaba usando el registro
            variable_registers[variable] = released_register  # Asigna el registro liberado a la nueva variable
            return registers[released_register]  # Retorna el valor del registro liberado
        raise Exception("No hay más registros disponibles")  # Lanza una excepción si no hay registros disponibles
    
    def validate_and_generate_code(self, intermediate_code):
        # Valida y genera código binario para cada línea de código intermedio
        for line in intermediate_code:
            tokens = line.split()  # Divide la línea en tokens
            if self.is_valid_assignment_constant(tokens):
                self.generate_assignment_constant(tokens)  # Genera código para asignación constante
            elif self.is_valid_assignment_variable(tokens):
                self.generate_assignment_variable(tokens)  # Genera código para asignación de variable
            elif self.is_valid_operation(tokens):
                self.handle_operation(tokens)  # Maneja operaciones aritméticas y lógicas
            else:
                print(f"Formato desconocido de línea de código intermedio: {line}")
                raise ValueError(f"Formato incorrecto en línea: {line}")

    def is_valid_assignment_constant(self, tokens):
        # Verifica si la línea es una asignación de constante
        return len(tokens) == 3 and tokens[1] == '=' and tokens[2].isdigit()

    def is_valid_assignment_variable(self, tokens):
        # Verifica si la línea es una asignación de variable
        return len(tokens) == 3 and tokens[1] == '=' and not tokens[2].isdigit()

    def is_valid_operation(self, tokens):
        # Verifica si la línea es una operación válida
        if len(tokens) == 5 and tokens[1] == '=' and tokens[3] in ('+', '*', '-', '/', '^', '<', '<=', '>', '>=', '==', '!='):
            return True
        if len(tokens) == 4 and tokens[1] == '=' and tokens[2] in ('sqrt', 'log'):
            return True
        return False

    def generate_assignment_constant(self, tokens):
        # Genera código binario para una asignación de constante a un registro
        dest_register = self.get_register(tokens[0])
        if isinstance(dest_register, int):
            self.binary_code.append(MOV_REG_CONST)  # Añade la instrucción de mover constante
            self.binary_code.append(dest_register)  # Añade el registro de destino
            self.binary_code.append(int(tokens[2]))  # Añade el valor constante
        else:
            raise Exception("No hay más registros disponibles")

    def generate_assignment_variable(self, tokens):
        # Genera código binario para una asignación de variable a un registro
        self.binary_code.append(MOV_REG_REG)  # Añade la instrucción de mover registro
        self.binary_code.append(self.get_register(tokens[0]))  # Añade el registro de destino
        self.binary_code.append(self.get_register(tokens[2]))  # Añade el registro de origen

    def handle_operation(self, tokens):
        # Maneja la generación de código para operaciones
        dest = self.get_register(tokens[0])
        op = tokens[2] if len(tokens) == 4 else tokens[3]
        
        if op in ('+', '-', '*', '/', '^'):
            src1 = self.get_register(tokens[2])
            src2 = self.get_register(tokens[4])
            if op == '+':
                self.binary_code.append(ADD_REG_REG)  # Añade la instrucción de suma
            elif op == '-':
                self.binary_code.append(SUB_REG_REG)  # Añade la instrucción de resta
            elif op == '*':
                self.binary_code.append(MUL_REG_REG)  # Añade la instrucción de multiplicación
            elif op == '/':
                self.binary_code.append(DIV_REG_REG)  # Añade la instrucción de división
            elif op == '^':
                self.binary_code.append(POW_REG_REG)  # Añade la instrucción de potencia
            
            self.binary_code.append(dest)  # Añade el registro de destino
            self.binary_code.append(src1)  # Añade el primer operando
            self.binary_code.append(src2)  # Añade el segundo operando
            
            if 'temp' in tokens[2]:
                self.release_register(tokens[2])  # Libera el registro temporal si es necesario
            if 'temp' in tokens[4]:
                self.release_register(tokens[4])  # Libera el registro temporal si es necesario
        
        elif op in ('<', '<=', '>', '>=', '==', '!='):
            src1 = self.get_register(tokens[2])
            src2 = self.get_register(tokens[4])
            self.binary_code.append(CMP_REG_REG)  # Añade la instrucción de comparación
            self.binary_code.append(dest)  # Añade el registro de destino
            self.binary_code.append(src1)  # Añade el primer operando
            self.binary_code.append(src2)  # Añade el segundo operando
            
            if 'temp' in tokens[2]:
                self.release_register(tokens[2])  # Libera el registro temporal si es necesario
            if 'temp' in tokens[4]:
                self.release_register(tokens[4])  # Libera el registro temporal si es necesario
        
        elif op == 'sqrt':
            src = self.get_register(tokens[3])
            self.binary_code.append(SQRT_REG)  # Añade la instrucción de raíz cuadrada
            self.binary_code.append(dest)  # Añade el registro de destino
            self.binary_code.append(src)  # Añade el operando
            
            if 'temp' in tokens[3]:
                self.release_register(tokens[3])  # Libera el registro temporal si es necesario
        
        elif op == 'log':
            src = self.get_register(tokens[3])
            self.binary_code.append(LOG_REG)  # Añade la instrucción de logaritmo
            self.binary_code.append(dest)  # Añade el registro de destino
            self.binary_code.append(src)  # Añade el operando
            
            if 'temp' in tokens[3]:
                self.release_register(tokens[3])  # Libera el registro temporal si es necesario

    def release_register(self, variable):
        # Libera un registro temporal asociado a una variable
        if variable in variable_registers:
            reg = variable_registers[variable]
            del variable_registers[variable]  # Elimina la variable del diccionario
            self.used_registers.remove(reg)  # Marca el registro como libre

    def get_binary_code(self):
        # Retorna el código binario generado
        return self.binary_code
