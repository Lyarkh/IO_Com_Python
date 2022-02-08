try:
    arquivo_contato = open('src/data/nao-existe.csv', encoding='latin_1')

    for linha in arquivo_contato:
        print(linha, end= '')
except FileNotFoundError:
    print('Arquivo não encontrado')
finally:
    arquivo_contato.close()