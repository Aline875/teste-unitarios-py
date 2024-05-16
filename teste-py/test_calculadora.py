import pytest
from calculadora import adicao, subtracao, multiplicacao, divisao

def test_adicao():
    assert adicao(2, 3) == 5
    assert adicao(-1, 1) == 0
    assert adicao(-1, -1) == -2

def test_subtracao():
    assert subtracao(2, 3) == -1
    assert subtracao(-1, 1) == -2
    assert subtracao(-1, -1) == 0

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(-1, 1) == -1
    assert multiplicacao(-1, -1) == 1

def test_divisao():
    assert divisao(6, 3) == 2
    assert divisao(-1, 1) == -1
    assert divisao(-1, -1) == 1
    with pytest.raises(ValueError):
        divisao(1, 0)
