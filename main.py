from lexer import probar_lexer

# Código de prueba

codigo_prueba_1 = """
qubit q0
entero num = 5
booleano flag = verdadero
si (num > 3) {
    imprimir num + 1
} sino {
    medir q0
}
X q0
CNOT q0, q1
"""

codigo_prueba_2 = """
entero x = 10 @ 5
booleano flag = verdadero #
si (x <= 0) {
    imprimir x
}
"""

codigo_prueba_3 = """
entero resultado = 3 + 5 * (2 - 1) / 4
imprimir resultado
"""

if __name__ == "__main__":

    print("Tokens reconocidos:\n")
    probar_lexer(codigo_prueba_2)