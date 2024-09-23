# Quantum

Quantum es un lenguaje de programación simplificado diseñado 
para introducir conceptos de computación cuántica.
____________
____________

### Características Principales

+ **Sintaxis simple y clara**: Quantum está diseñado para ser fácil de leer y escribir, con una sintaxis clara y concisa.
+ ***Operaciones*** cuánticas básicas.
+ ***Simulación*** de circuitos cuánticos básicos.
+ ***Estructuras*** de control clásicas (condicionales e iteradores)
+ ***Lenguaje*** base Python.

### Componentes Básicos

1 - **Qubit**: Un qubit es la unidad básica de información cuántica.

```python
qubit q1 = |0>
qubit q2 = |1>
```

2 - **Puertas Cuánticas**: Las puertas cuánticas son operaciones que se aplican a los qubits.

```python
H(q1)  # Puerta Hadamard
CNOT(q1, q2)  # Puerta CNOT
```

3 - **Medición**: La medición de un qubit colapsa su estado cuántico a un estado clásico.

```python
result = medir(q1)
```

4 - **Estructuras de Control**: Quantum admite estructuras de control clásicas.

```python
if (medir(q1) == 1) {
    X(q2)
}
```

5 - **Iteradores**: Quantum admite bucles clásicos.

```python
for i in range(3) {
    H(q[i])
}
```

### Ejemplo de Programa

#### Algoritmo de Deutsch
***Propósito***:
+ El algoritmo de Deutsch resuelve un problema específico: 
determinar si una función booleana de un bit es constante o balanceada, 
y lo hace con una sola evaluación de la función. 
+ Definiciones:

- Una función booleana f(x) que toma un bit de entrada y produce un bit de salida.
- Constante: f(0) = f(1) (ambos 0 o ambos 1)
- Balanceada: f(0) ≠ f(1) (uno es 0 y el otro es 1)

#### Problema clásico vs. cuántico:

+ Clásicamente: necesitarías evaluar f(0) y f(1) y compararlos, lo que requiere dos evaluaciones.
+ Cuánticamente: el algoritmo de Deutsch puede determinar si f es constante o balanceada con una sola evaluación.

```mermaid
graph LR
A["|0〉"] --> H1[H]
B["|1〉"] --> H2[H]
H1 --> U[Uf]
H2 --> U
U --> H3[H]
U --> M2[M]
H3 --> M1[M]
style A fill:#f9f,stroke:#333,stroke-width:2px
style B fill:#f9f,stroke:#333,stroke-width:2px
style H1 fill:#ccf,stroke:#333,stroke-width:2px
style H2 fill:#ccf,stroke:#333,stroke-width:2px
style H3 fill:#ccf,stroke:#333,stroke-width:2px
style U fill:#fcc,stroke:#333,stroke-width:2px
style M1 fill:#cfc,stroke:#333,stroke-width:2px
style M2 fill:#cfc,stroke:#333,stroke-width:2px

```

    
```python
# Inicialización de qubits
qubit q1 = |0>
qubit q2 = |1>

# Función booleana
function esBalanceado(control, target) {
    CNOT(control, target)
}

# Algoritmo de Deutsch
H(q1)
H(q2)

esBalancedo(q1, q2)

H(q1)

result = medir(q1)

if (result == 0) {
    print("La función es constante")
} else {
    print("La función es balanceada")
}
```

# Algoritmos Cuánticos Sencillos

***Generador de Bits Aleatorios Cuántico***
   
_Explicación_:
Este algoritmo aprovecha la naturaleza probabilística de la mecánica cuántica para generar bits aleatorios verdaderos. Se basa en el principio de superposición y el colapso de la función de onda durante la medición.

### Cómo funciona:

* Inicializamos un qubit en el estado |0>.
Aplicamos una puerta Hadamard (H) para poner el qubit en superposición.
Medimos el qubit, obteniendo 0 o 1 con igual probabilidad.
Repetimos el proceso para generar múltiples bits aleatorios.

***Teleportación Cuántica Simplificada***
   
_Explicación:_
La teleportación cuántica permite "transferir" el estado de un qubit a otro qubit distante utilizando entrelazamiento y comunicación clásica. Esta versión simplificada muestra los principios básicos sin la comunicación clásica.
   
### Cómo funciona:

Preparamos un estado a teleportar en un qubit.
Creamos un par de qubits entrelazados (estado Bell).
Realizamos una operación de entrelazamiento entre el qubit a teleportar y uno del par entrelazado.
Medimos los dos primeros qubits.
El estado original se "teleporta" al tercer qubit (en un experimento real, se necesitaría comunicación clásica y operaciones adicionales).

# Especificación Léxica del Lenguaje Quantum

## Tabla de Tokens, Lexemas y Patrones

| Token          | Lexema(s)              | Patrón (Regex)         |
|----------------|------------------------|------------------------|
| QUBIT          | "qubit"                | bqubit                 |
| MEDIR          | "medir"                | medir                  |
| SI             | "si"                   | si                     |
| ENTONCES       | "entonces"             | entonces               |
| MIENTRAS       | "mientras"             | mientras               | |
| PRINT          | "print"                | bprint                 |
| ESTADO_QUBIT   | "estado_qubit"         |                        |1>"                | \|[01]>                     |                |X|CNOT)\b              |
| VARIABLE       | (nombres de variables) | [a-zA-Z_][a-zA-Z0-9_]* |
| NUMERO         | (números enteros)      | [0-9]*                 |
| IGUAL          | "="                    | =                      |
| SUMA           | "+"                    | \+                     |
| RESTA          | "-"                    | -                      |
| MULTIPLICACION | "*"                    | \*                     |
| DIVISION       | "/"                    | /                      |
| LPAREN         | "("                    | \(                     |
| RPAREN         | ")"                    | \)                     |
| LBRACKET       | "["                    | \[                     |
| RBRACKET       | "]"                    | \]                     |
| COMA           | ","                    | ,                      |
| DOSPUNTOS      | ":"                    | :                      | |




## Funcion de Tokenizacion

import re

# Definir los patrones de los tokens usando expresiones regulares
token_specification = [
    ('QUBIT', r'\bqubit\b'),           # Qubit keyword
    ('MEDIR', r'\bmedir\b'),           # Medir keyword
    ('SI', r'\bsi\b'),                 # Condicional 'si'
    ('ENTONCES', r'\bentonces\b'),     # 'entonces' keyword
    ('MIENTRAS', r'\bmientras\b'),     # Loop 'mientras'
    ('PRINT', r'\bprint\b'),           # Print keyword
    ('ESTADO_QUBIT', r'\|[01]\>'),     # Estado de qubit (|0>, |1>)
    ('VARIABLE', r'[a-zA-Z_][a-zA-Z0-9_]*'), # Nombres de variables
    ('NUMERO', r'[0-9]+'),             # Números enteros
    ('IGUAL', r'='),                   # Signo de igualdad
    ('SUMA', r'\+'),                   # Operador de suma
    ('RESTA', r'-'),                   # Operador de resta
    ('MULTIPLICACION', r'\*'),         # Operador de multiplicación
    ('DIVISION', r'/'),                # Operador de división
    ('LPAREN', r'\('),                 # Paréntesis izquierdo
    ('RPAREN', r'\)'),                 # Paréntesis derecho
    ('LBRACKET', r'\['),               # Corchete izquierdo
    ('RBRACKET', r'\]'),               # Corchete derecho
    ('COMA', r','),                    # Coma
    ('DOSPUNTOS', r':'),               # Dos puntos
    ('SKIP', r'[ \t]+'),               # Ignorar espacios y tabulaciones
    ('NEWLINE', r'\n'),                # Nueva línea
    ('MISMATCH', r'.'),                # Cualquier otro carácter
]

# Compilar la especificación de tokens
token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)

# Función de tokenización
def tokenize(code):
    tokens = []
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMERO':
            value = int(value)  # Convertir números a enteros
        elif kind == 'NEWLINE':
            continue  # Ignorar saltos de línea
        elif kind == 'SKIP':
            continue  # Ignorar espacios y tabulaciones
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Error de síntaxis: {value}')
        tokens.append((kind, value))
    return tokens

# Ejemplo de código en Quantum
code = '''
qubit q1 = |0>
qubit q2 = |1>
H(q1)
CNOT(q1, q2)
result = medir(q1)
if (result == 1) {
    X(q2)
}
'''

# Tokenizar el código
tokens = tokenize(code)
for token in tokens:
    print(token)


Cuando se ejecuta el codigo, debería producir una lista de tokens que representan cada elemento del código, palabras clave, variables, y operadores.

Si se ejecuta la salida seria algo similar a esto:

plaintext
Copiar código
('QUBIT', 'qubit')
('VARIABLE', 'q1')
('IGUAL', '=')
('ESTADO_QUBIT', '|0>')
('QUBIT', 'qubit')
('VARIABLE', 'q2')
('IGUAL', '=')
('ESTADO_QUBIT', '|1>')
('VARIABLE', 'H')
('LPAREN', '(')
('VARIABLE', 'q1')
('RPAREN', ')')
('VARIABLE', 'CNOT')
('LPAREN', '(')
('VARIABLE', 'q1')
('COMA', ',')
('VARIABLE', 'q2')
('RPAREN', ')')
('VARIABLE', 'result')
('IGUAL', '=')
('MEDIR', 'medir')
('LPAREN', '(')
('VARIABLE', 'q1')
('RPAREN', ')')
('SI', 'if')
('LPAREN', '(')
('VARIABLE', 'result')
('IGUAL', '=')
('NUMERO', 1)
('RPAREN', ')')
('LBRACKET', '{')
('VARIABLE', 'X')
('LPAREN', '(')
('VARIABLE', 'q2')
('RPAREN', ')')
('RBRACKET', '}')

## Próximos pasos:

1. Implementar una función de tokenización que utilice estos patrones para convertir el código fuente en una serie de tokens.
2. Manejar casos especiales como la indentación y los comentarios.
3. Implementar el manejo de errores para caracteres o patrones no reconocidos.
