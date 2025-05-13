with open("relatorio.txt", "r", encoding="utf-8") as arquivo:

    linhas = arquivo.readlines()

limpar_linhas = []

for linha in linhas:
    linha = linha.strip()
    if linha:
        linha = linha.capitalize()
        limpar_linhas.append(linha)
palavra_chave = ["erro", "sucesso", "falha", "cliente", "produto"]
contar_chave = {palavra: 0 for palavra in palavra_chave}
frases_chaves = []

for linha in limpar_linhas:
    linha_lower = linha.lower()        

for palavra in palavra_chave:
    if palavra in linha_lower:
        contar_chave[palavra] += 1
        frases_chaves.append(linha)
        break
print(contar_chave)
for palavra, quantidade in contar_chave.items():
    print(f"{palavra}: {quantidade}")

print("Frases com palavras-chave: ")
for frase in frases_chaves:
    print(frase)
with open("frases_chaves.txt", "w", encoding="utf-8") as arquivo_chave:
    for frase in frases_chaves:
        arquivo_chave.write(frase + "\n")
