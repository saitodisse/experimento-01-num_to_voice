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
    if len(partes) == 1:
        return partes[0]
    elif len(partes) == 2:
        # Se a segunda parte for menor que 100 ou for exatamente 100, usa "e"
        if (partes[0].endswith("milhão") or partes[0].endswith("milhões")) and \
           (partes[1] == "mil" or partes[1].endswith(" mil")):
            return f"{partes[0]} e {partes[1]}"
        elif partes[1] == "cem" or (len(partes[1]) <= 3 or partes[1].startswith("dez") or \
             partes[1].startswith("onze") or partes[1].startswith("doze") or \
             partes[1].startswith("treze") or partes[1].startswith("quatorze") or \
             partes[1].startswith("quinze") or partes[1].startswith("dezesseis") or \
             partes[1].startswith("dezessete") or partes[1].startswith("dezoito") or \
             partes[1].startswith("dezenove")):
            return f"{partes[0]} e {partes[1]}"
        else:
            return f"{partes[0]} {partes[1]}"
    else:  # len(partes) == 3
        if milhares == 0:
            return f"{partes[0]} e {partes[2]}"
        elif centenas < 100 or centenas == 100:
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
                
            numero = int(entrada)
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