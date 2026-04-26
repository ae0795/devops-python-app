import time


def saudacao(nome: str) -> str:
    return f"Olá, Antony! Bem-vindo ao projeto de DevOps com Python."


def despedida(nome: str) -> str:
    return f"Até logo, Antony!"


def somar(a: int, b: int) -> int:
    return a + b


def multiplicar(a: int, b: int) -> int:
    return a * b


def eh_par(numero: int) -> bool:
    return numero % 2 == 0


if __name__ == "__main__":
    print(saudacao("Antony"))
    print(despedida("Antony"))