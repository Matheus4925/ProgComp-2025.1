import random
palavras = (
    "ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
)
palavras2 = ( 
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"
)

segredo = palavras[random.randint(0,len(palavras)-1)]
segredo2 = palavras2[random.randint(0,len(palavras2)-1)]
tentativas = 0
acertos = 0

Palavras_digitidas = list()

Ndescoberto = True
Ndescoberto2 = True

while (tentativas < 7) and (acertos != 2):
    while True:
        palavra = input("Digite uma palavra:")
        palavra = palavra.upper()
        if len(palavra) != 5:
            print("Palavra inválida!")
            continue
        if palavra in Palavras_digitidas:
            print("Você já digitou essa palavra!")
            continue
        else:
            break
    
    Palavras_digitidas.append(palavra)
    resultado = ""
    resultado2 = ""
    if Ndescoberto == True:
        for pos in range(len(segredo)):
            if palavra[pos] == segredo[pos]:
                resultado += f"\033[1;42m{palavra[pos]}\033[0m"  # Verde (letra correta na posição certa)
            elif palavra[pos] in segredo:
                resultado += f"\033[1;43m{palavra[pos]}\033[0m"  # Amarelo (letra está na palavra, mas posição errada)
            else:
                resultado += f"\033[1;40m{palavra[pos]}\033[0m"  # Preto (letra errada)
        print(resultado)

    if Ndescoberto2 == True:
        for pos in range(len(segredo2)):
            if palavra[pos] == segredo2[pos]:
                resultado2 += f"\033[1;42m{palavra[pos]}\033[0m"  
            elif palavra[pos] in segredo2:
                resultado2 += f"\033[1;43m{palavra[pos]}\033[0m"  
            else:
                resultado2 += f"\033[1;40m{palavra[pos]}\033[0m"  
        print(resultado2)

    tentativas += 1
    print(f"Tentativas: {tentativas}")

    if Ndescoberto == True and palavra == segredo:
        acertos += 1
        Ndescoberto = False
        print("Você acertou a primeira palavra!")
    if Ndescoberto2 == True and palavra == segredo2:
        acertos += 1
        Ndescoberto2 = False
        print("Você acertou a segunda palavra!")

if acertos == 2:
    print(f"Parabéns! Você descobriu as palavras em {tentativas} tentativas!")
    if tentativas == 1:
        print("Impossível!")
    if tentativas == 2:
        print("Ninja!")
    if tentativas == 3:
        print("Impressionante!")
    if tentativas == 4:
        print("Interessante.")
    if tentativas == 5:
        print("Pode melhorar.")
    if tentativas == 6:
        print("Foi por pouco.")
else:
    print("Suas tentivativas acabaram!")
    print(f"As palavras eram: {segredo} e {segredo2}")
