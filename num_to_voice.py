def converter_numero_para_palavras(numero):
    if not isinstance(numero, int) or numero < 0 or numero > 999999999:
        raise ValueError("O número deve ser um inteiro entre 0 e 999.999.999")

    if numero == 0:
        return "zero"

    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centenas_lista = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

    def converter_grupo_de_tres(n):
        if n == 0:
            return ""
        
        # Caso especial para 100
        if n == 100:
            return "cem"
            
        resultado = ""
        
        # Tratamento das centenas
        if n >= 100:
            resultado = centenas_lista[n // 100]
            n = n % 100
            if n > 0:
                resultado += " e "
        
        # Tratamento das dezenas e unidades
        if n > 0:
            if n >= 20:
                resultado += dezenas[n // 10]
                if n % 10 > 0:
                    resultado += " e " + unidades[n % 10]
            elif n >= 10:
                resultado += especiais[n - 10]
            else:
                resultado += unidades[n]
            
        return resultado

    # Separar milhões, milhares e centenas
    milhoes = numero // 1000000
    resto = numero % 1000000
    milhares = resto // 1000
    centenas = resto % 1000

    partes = []

    # Processar milhões
    if milhoes > 0:
        if milhoes == 1:
            partes.append("um milhão")
        else:
            partes.append(converter_grupo_de_tres(milhoes) + " milhões")

    # Processar milhares
    if milhares > 0:
        if milhares == 1:
            partes.append("mil")
        else:
            partes.append(converter_grupo_de_tres(milhares) + " mil")

    # Processar centenas
    if centenas > 0:
        partes.append(converter_grupo_de_tres(centenas))

    # Juntar as partes com os conectivos apropriados
    if len(partes) == 0:
        return "zero"
    elif len(partes) == 1:
        return partes[0]
    elif len(partes) == 2:
        # Se a segunda parte for menor que 100 ou for exatamente 100, usa "e"
        if (len(partes[1]) <= 3 or partes[1] == "cem") and not "mil" in partes[1]:
            return f"{partes[0]} e {partes[1]}"
        # Se a primeira parte termina com "mil", não usa "e"
        elif "mil" in partes[0]:
            return f"{partes[0]} {partes[1]}"
        else:
            return f"{partes[0]} e {partes[1]}"
    else:  # len(partes) == 3
        # Se a última parte for menor que 100 ou for exatamente 100, usa "e"
        if len(partes[2]) <= 3 or partes[2] == "cem":
            return f"{partes[0]} {partes[1]} e {partes[2]}"
        else:
            return f"{partes[0]} {partes[1]} {partes[2]}"

    return resultado

def main():
    print("Conversor de Números para Extenso")
    print("=================================")
    print("Digite um número entre 0 e 999.999.999 para ver como ele é escrito por extenso")
    print("Digite 'sair' para encerrar o programa")
    print()

    while True:
        try:
            entrada = input("Digite um número: ").strip()
            
            if entrada.lower() in ['sair', 'exit', 'quit', 'q']:
                print("\nObrigado por usar o conversor!")
                break
                
            if not entrada:
                print("Por favor, digite um número.")
                continue
                
            numero = float(entrada)
            resultado = converter_numero_para_palavras(numero)
            print(f"\n{numero:,} por extenso é:".replace(",", "."))
            print(f"➜ {resultado}")
            print()
            
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                print("Erro: Digite apenas números inteiros.")
            else:
                print(f"Erro: {e}")
            print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma encerrado pelo usuário.")

def num_to_voice(numero):
    if not isinstance(numero, (int, float)):
        raise ValueError("O número deve ser um inteiro ou float")
    
    # Tratar números negativos
    if numero < 0:
        return "menos " + num_to_voice(abs(numero))
    
    if abs(int(numero)) > 999:
        raise ValueError("Parte inteira fora do intervalo suportado (-999 a 999)")
    
    # Separar parte inteira e decimal
    parte_inteira = int(numero)
    parte_decimal = abs(numero) - abs(int(numero))
    
    # Converter parte inteira
    resultado = []
    if parte_inteira == 0 and parte_decimal == 0:
        return "zero"
    
    if parte_inteira == 0:
        resultado.append("zero")
    else:
        resultado.append(converter_inteiro(parte_inteira))
    
    # Converter parte decimal se existir
    if parte_decimal > 0:
        # Converter para string e remover o "0."
        decimal_str = f"{parte_decimal:.20f}".split('.')[1]
        # Limitar a 20 casas decimais
        decimal_str = decimal_str[:20].rstrip('0')
        
        if decimal_str:
            resultado.append("vírgula")
            
            # Processar cada dígito individualmente
            for digito in decimal_str:
                resultado.append("zero" if digito == "0" else converter_inteiro(int(digito)))
    
    return " ".join(resultado)

def converter_inteiro(numero):
    if numero == 0:
        return "zero"
        
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas_especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
    
    # Tratamento especial para 100
    if numero == 100:
        return "cem"
    
    # Separar o número em centenas, dezenas e unidades
    centena = numero // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10
    
    resultado = []
    
    # Adicionar centenas
    if centena > 0:
        resultado.append(centenas[centena])
    
    # Tratar dezenas
    if dezena == 1:
        # Caso especial para números de 10-19
        if len(resultado) > 0:
            resultado.append("e")
        resultado.append(dezenas_especiais[unidade])
        return " ".join(resultado)
    
    # Adicionar dezenas (exceto quando é zero)
    if dezena > 1:
        if len(resultado) > 0:
            resultado.append("e")
        resultado.append(dezenas[dezena])
    
    # Adicionar unidades (exceto quando é zero)
    if unidade > 0 and dezena != 1:
        if len(resultado) > 0:
            resultado.append("e")
        resultado.append(unidades[unidade])
    
    return " ".join(resultado)

def number_to_words(number):
    unidades = {
        0: "zero",
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove"
    }
    
    especiais = {
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove"
    }

    dezenas = {
        2: "vinte",
        3: "trinta",
        4: "quarenta",
        5: "cinquenta",
        6: "sessenta",
        7: "setenta",
        8: "oitenta",
        9: "noventa"
    }

    centenas = {
        1: "cento",
        2: "duzentos",
        3: "trezentos",
        4: "quatrocentos",
        5: "quinhentos",
        6: "seiscentos",
        7: "setecentos",
        8: "oitocentos",
        9: "novecentos"
    }

    # Tratamento de números negativos
    if number < 0:
        return "menos " + number_to_words(abs(number))

    # Tratamento de números decimais
    if isinstance(number, float):
        partes = str(number).split('.')
        parte_inteira = int(partes[0])
        parte_decimal = partes[1]
        
        resultado = number_to_words(parte_inteira)
        
        if parte_decimal:
            resultado += " vírgula"
            for digito in parte_decimal:
                resultado += " " + unidades[int(digito)]
        return resultado

    # Caso especial para 100
    if number == 100:
        return "cem"

    # Números inteiros
    if number <= 9:
        return unidades[number]
    elif number <= 19:
        return especiais[number]
    elif number <= 99:
        dezena = number // 10
        unidade = number % 10
        if unidade == 0:
            return dezenas[dezena]
        return f"{dezenas[dezena]} e {unidades[unidade]}"
    else:  # 100-999
        centena = number // 100
        resto = number % 100
        if resto == 0:
            return centenas[centena]
        return f"{centenas[centena]} e {number_to_words(resto)}" 