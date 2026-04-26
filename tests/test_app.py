import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import saudacao, despedida, somar, multiplicar, eh_par


def test_saudacao():
    assert saudacao("Antony") == "Olá, Antony! Bem-vindo ao projeto de DevOps com Python."


def test_despedida():
    assert despedida("Antony") == "Até logo, Antony!"


def test_somar():
    assert somar(2, 3) == 5


def test_multiplicar():
    assert multiplicar(4, 5) == 20


def test_eh_par():
    assert eh_par(8) is True