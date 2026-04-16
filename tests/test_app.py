from app import saudacao, despedida


def test_saudacao():
    assert saudacao("Antony") == "Olá, Antony! Bem-vindo ao projeto de DevOps com Python."


def test_despedida():
    assert despedida("Antony") == "Até logo, Antony!"