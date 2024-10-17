# Función para probar el lexer
from scanner import lexer


def probar_lexer(codigo):
    lexer.input(codigo)  # Enviar el código fuente al lexer
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f'Tipo: {tok.type}, Valor: {tok.value}, Línea: {tok.lineno}, Posición: {tok.lexpos}')



