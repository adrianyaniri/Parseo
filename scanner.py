import ply.lex as lex

# Definir tokens
tokens = (
    'QUBIT', 'ENTERO', 'BOOLEANO', 'SI', 'SINO', 'MIENTRAS', 'DEF', 'IMPRIMIR', 'MEDIR',
    'H', 'X', 'CNOT', 'IDENTIFICADOR', 'NUMERO', 'ESTADO_QUBIT', 'IGUAL',
    'PARENTESIS_IZQ', 'PARENTESIS_DER', 'LLAVE_IZQ', 'LLAVE_DER', 'COMA', 'MAS', 'MENOS',
    'POR', 'DIVIDIDO', 'VERDADERO', 'FALSO'
)

# Reglas para tokens simples
t_IGUAL = r'='
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_COMA = r','
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'

# Ignorar espacios, tabulaciones y comentarios
t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

# Palabras clave con una función genérica para reducir código
reserved = {
    'qubit': 'QUBIT',
    'entero': 'ENTERO',
    'booleano': 'BOOLEANO',
    'si': 'SI',
    'sino': 'SINO',
    'mientras': 'MIENTRAS',
    'def': 'DEF',
    'imprimir': 'IMPRIMIR',
    'medir': 'MEDIR',
    'H': 'H',
    'X': 'X',
    'CNOT': 'CNOT',
    'verdadero': 'VERDADERO',
    'falso': 'FALSO'
}

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFICADOR')  # Verificar si es palabra reservada
    return t

# Números
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Estado de qubits
def t_ESTADO_QUBIT(t):
    r'\|[01]>'
    return t

# Manejar nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejar errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lexer.lineno}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
