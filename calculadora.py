def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError(
            "El divisor no puede ser cero. Proporciona un número distinto de 0."
        )
    return a / b


def potencia(a, b):
    return a ** b


def funcion_nueva_con_bug():
    return 1 / 0
