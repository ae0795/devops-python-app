import time


def saudacao(nome: str) -> str:
    return f"Olá, {nome}! Bem-vindo ao projeto de DevOps com Python."


def despedida(nome: str) -> str:
    return f"Até logo, {nome}!"


if __name__ == "__main__":
    print(saudacao("Antony"))
    print(despedida("Antony"))
    time.sleep(300)