import pytest
from num_to_voice import converter_numero_para_palavras
import unittest
from num_to_voice import num_to_voice
from num_to_voice import number_to_words

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

class TestNumToVoice(unittest.TestCase):
    def test_numeros_basicos(self):
        casos_teste = {
            0: "zero",
            1: "um",
            2: "dois",
            3: "três",
            4: "quatro",
            5: "cinco",
            6: "seis",
            7: "sete",
            8: "oito",
            9: "nove",
            10: "dez",
            11: "onze",
            12: "doze",
            13: "treze",
            14: "quatorze",
            15: "quinze",
            16: "dezesseis",
            17: "dezessete",
            18: "dezoito",
            19: "dezenove",
            20: "vinte"
        }
        
        for numero, esperado in casos_teste.items():
            with self.subTest(numero=numero):
                self.assertEqual(num_to_voice(numero), esperado)
                
    def test_dezenas(self):
        casos_teste = {
            30: "trinta",
            40: "quarenta",
            50: "cinquenta",
            60: "sessenta",
            70: "setenta",
            80: "oitenta",
            90: "noventa",
            21: "vinte e um",
            35: "trinta e cinco",
            48: "quarenta e oito",
            99: "noventa e nove"
        }
        
        for numero, esperado in casos_teste.items():
            with self.subTest(numero=numero):
                self.assertEqual(num_to_voice(numero), esperado)
                
    def test_centenas(self):
        casos_teste = {
            100: "cem",
            101: "cento e um",
            110: "cento e dez",
            111: "cento e onze",
            199: "cento e noventa e nove",
            200: "duzentos",
            201: "duzentos e um",
            300: "trezentos",
            400: "quatrocentos",
            500: "quinhentos",
            600: "seiscentos",
            700: "setecentos",
            800: "oitocentos",
            900: "novecentos",
            999: "novecentos e noventa e nove"
        }
        
        for numero, esperado in casos_teste.items():
            with self.subTest(numero=numero):
                self.assertEqual(num_to_voice(numero), esperado)

    def test_numeros_negativos(self):
        casos_teste = {
            -1: "menos um",
            -10: "menos dez",
            -15: "menos quinze",
            -20: "menos vinte",
            -21: "menos vinte e um",
            -100: "menos cem",
            -101: "menos cento e um",
            -999: "menos novecentos e noventa e nove"
        }
        
        for numero, esperado in casos_teste.items():
            with self.subTest(numero=numero):
                self.assertEqual(num_to_voice(numero), esperado)

    def test_numeros_decimais(self):
        casos_teste = {
            0.5: "zero vírgula cinco",
            1.0: "um",
            1.1: "um vírgula um",
            1.23: "um vírgula vinte e três",
            10.01: "dez vírgula zero um",
            100.001: "cem vírgula zero zero um",
            -1.5: "menos um vírgula cinco",
            -10.05: "menos dez vírgula zero cinco",
            0.01: "zero vírgula zero um",
            0.001: "zero vírgula zero zero um"
        }
        
        for numero, esperado in casos_teste.items():
            with self.subTest(numero=numero):
                self.assertEqual(num_to_voice(numero), esperado)

class TestNumberToWords(unittest.TestCase):
    def test_unidades(self):
        self.assertEqual(number_to_words(0), "zero")
        self.assertEqual(number_to_words(1), "um")
        self.assertEqual(number_to_words(2), "dois")
        self.assertEqual(number_to_words(3), "três")
        self.assertEqual(number_to_words(4), "quatro")
        self.assertEqual(number_to_words(5), "cinco")
        self.assertEqual(number_to_words(6), "seis")
        self.assertEqual(number_to_words(7), "sete")
        self.assertEqual(number_to_words(8), "oito")
        self.assertEqual(number_to_words(9), "nove")

    def test_dezenas(self):
        self.assertEqual(number_to_words(10), "dez")
        self.assertEqual(number_to_words(11), "onze")
        self.assertEqual(number_to_words(12), "doze")
        self.assertEqual(number_to_words(13), "treze")
        self.assertEqual(number_to_words(14), "quatorze")
        self.assertEqual(number_to_words(15), "quinze")
        self.assertEqual(number_to_words(16), "dezesseis")
        self.assertEqual(number_to_words(17), "dezessete")
        self.assertEqual(number_to_words(18), "dezoito")
        self.assertEqual(number_to_words(19), "dezenove")
        self.assertEqual(number_to_words(20), "vinte")

    def test_dezenas_compostas(self):
        self.assertEqual(number_to_words(21), "vinte e um")
        self.assertEqual(number_to_words(35), "trinta e cinco")
        self.assertEqual(number_to_words(48), "quarenta e oito")
        self.assertEqual(number_to_words(99), "noventa e nove")

    def test_centenas(self):
        self.assertEqual(number_to_words(100), "cem")
        self.assertEqual(number_to_words(101), "cento e um")
        self.assertEqual(number_to_words(110), "cento e dez")
        self.assertEqual(number_to_words(199), "cento e noventa e nove")
        self.assertEqual(number_to_words(200), "duzentos")
        self.assertEqual(number_to_words(999), "novecentos e noventa e nove")

    def test_numeros_negativos(self):
        self.assertEqual(number_to_words(-1), "menos um")
        self.assertEqual(number_to_words(-15), "menos quinze")
        self.assertEqual(number_to_words(-20), "menos vinte")
        self.assertEqual(number_to_words(-99), "menos noventa e nove")

    def test_numeros_decimais(self):
        self.assertEqual(number_to_words(1.5), "um vírgula cinco")
        self.assertEqual(number_to_words(0.1), "zero vírgula um")
        self.assertEqual(number_to_words(-1.1), "menos um vírgula um")
        self.assertEqual(number_to_words(10.01), "dez vírgula zero um")

if __name__ == '__main__':
    unittest.main() 