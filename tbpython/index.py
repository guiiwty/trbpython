import tkinter as tk
from tkinter import messagebox, scrolledtext

def processar_arquivo():
    try:
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

        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, "Contagem de palavras-chave:\n")
        for palavra, quantidade in contar_chave.items():
            resultado_text.insert(tk.END, f"{palavra}: {quantidade}\n")

        resultado_text.insert(tk.END, "\nFrases com palavras-chave:\n")
        for frase in frases_chaves:
            resultado_text.insert(tk.END, frase + "\n")

        global frases_salvas
        frases_salvas = frases_chaves

        messagebox.showinfo("Sucesso", "Arquivo processado com sucesso!")

    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo 'relatorio.txt' não encontrado!")

def salvar_frases():
    if not frases_salvas:
        messagebox.showwarning("Aviso", "Nenhuma frase para salvar. Primeiro processe o arquivo.")
        return

    with open("frases_chaves.txt", "w", encoding="utf-8") as arquivo_chave:
        for frase in frases_salvas:
            arquivo_chave.write(frase + "\n")
    messagebox.showinfo("Salvo", "Frases salvas em 'frases_chaves.txt'.")

janela = tk.Tk()
janela.title("Analisador de Relatório")
janela.geometry("500x500")

btn_processar = tk.Button(janela, text="Processar Relatório", command=processar_arquivo)
btn_processar.pack(pady=10)

btn_salvar = tk.Button(janela, text="Salvar Frases-Chave", command=salvar_frases)
btn_salvar.pack(pady=5)

resultado_text = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=60, height=20)
resultado_text.pack(padx=10, pady=10)

frases_salvas = []

janela.mainloop()
