import pytest
from num_to_voice import converter_numero_para_palavras

def test_zero():
    assert converter_numero_para_palavras(0) == "zero"

def test_unidades():
    assert converter_numero_para_palavras(1) == "um"
    assert converter_numero_para_palavras(2) == "dois"
    assert converter_numero_para_palavras(5) == "cinco"
    assert converter_numero_para_palavras(9) == "nove"

def test_numeros_especiais_ate_20():
    assert converter_numero_para_palavras(10) == "dez"
    assert converter_numero_para_palavras(11) == "onze"
    assert converter_numero_para_palavras(15) == "quinze"
    assert converter_numero_para_palavras(20) == "vinte"

def test_dezenas():
    assert converter_numero_para_palavras(30) == "trinta"
    assert converter_numero_para_palavras(42) == "quarenta e dois"
    assert converter_numero_para_palavras(99) == "noventa e nove"

def test_centenas():
    assert converter_numero_para_palavras(100) == "cem"
    assert converter_numero_para_palavras(101) == "cento e um"
    assert converter_numero_para_palavras(199) == "cento e noventa e nove"
    assert converter_numero_para_palavras(200) == "duzentos"
    assert converter_numero_para_palavras(999) == "novecentos e noventa e nove"

def test_casos_especiais_centenas():
    assert converter_numero_para_palavras(500) == "quinhentos"
    assert converter_numero_para_palavras(600) == "seiscentos"
    assert converter_numero_para_palavras(900) == "novecentos"
    assert converter_numero_para_palavras(110) == "cento e dez"
    assert converter_numero_para_palavras(111) == "cento e onze"

def test_numeros_redondos():
    assert converter_numero_para_palavras(10) == "dez"
    assert converter_numero_para_palavras(20) == "vinte"
    assert converter_numero_para_palavras(30) == "trinta"
    assert converter_numero_para_palavras(40) == "quarenta"
    assert converter_numero_para_palavras(50) == "cinquenta"
    assert converter_numero_para_palavras(60) == "sessenta"
    assert converter_numero_para_palavras(70) == "setenta"
    assert converter_numero_para_palavras(80) == "oitenta"
    assert converter_numero_para_palavras(90) == "noventa"

def test_milhares():
    assert converter_numero_para_palavras(1000) == "mil"
    assert converter_numero_para_palavras(1001) == "mil e um"
    assert converter_numero_para_palavras(1100) == "mil e cem"
    assert converter_numero_para_palavras(1101) == "mil cento e um"
    assert converter_numero_para_palavras(1110) == "mil cento e dez"
    assert converter_numero_para_palavras(1111) == "mil cento e onze"
    assert converter_numero_para_palavras(2000) == "dois mil"
    assert converter_numero_para_palavras(2001) == "dois mil e um"
    assert converter_numero_para_palavras(10000) == "dez mil"
    assert converter_numero_para_palavras(11000) == "onze mil"
    assert converter_numero_para_palavras(15000) == "quinze mil"
    assert converter_numero_para_palavras(20000) == "vinte mil"
    assert converter_numero_para_palavras(999999) == "novecentos e noventa e nove mil novecentos e noventa e nove"

def test_milhoes():
    assert converter_numero_para_palavras(1000000) == "um milhão"
    assert converter_numero_para_palavras(2000000) == "dois milhões"
    assert converter_numero_para_palavras(1000001) == "um milhão e um"
    assert converter_numero_para_palavras(1000100) == "um milhão e cem"
    assert converter_numero_para_palavras(1001000) == "um milhão mil"
    assert converter_numero_para_palavras(1001001) == "um milhão mil e um"
    assert converter_numero_para_palavras(1020304) == "um milhão vinte mil trezentos e quatro"
    assert converter_numero_para_palavras(9999999) == "nove milhões novecentos e noventa e nove mil novecentos e noventa e nove"

def test_casos_especiais_milhoes():
    assert converter_numero_para_palavras(2000001) == "dois milhões e um"
    assert converter_numero_para_palavras(2100000) == "dois milhões cem mil"
    assert converter_numero_para_palavras(2100100) == "dois milhões cem mil e cem"
    assert converter_numero_para_palavras(2100101) == "dois milhões cem mil cento e um"
    assert converter_numero_para_palavras(2100001) == "dois milhões cem mil e um"

def test_centenas_de_milhoes():
    assert converter_numero_para_palavras(100000000) == "cem milhões"
    assert converter_numero_para_palavras(100000001) == "cem milhões e um"
    assert converter_numero_para_palavras(100100000) == "cem milhões cem mil"
    assert converter_numero_para_palavras(100100100) == "cem milhões cem mil e cem"
    assert converter_numero_para_palavras(999999999) == "novecentos e noventa e nove milhões novecentos e noventa e nove mil novecentos e noventa e nove"

def test_numeros_invalidos():
    with pytest.raises(ValueError):
        converter_numero_para_palavras(-1)
    with pytest.raises(ValueError):
        converter_numero_para_palavras(1000000000)
    with pytest.raises(ValueError):
        converter_numero_para_palavras(3.14)  # teste com float
    with pytest.raises(ValueError):
        converter_numero_para_palavras("123")  # teste com string 