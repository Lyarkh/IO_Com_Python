try:
    with open('src/data/contatos.csv', encoding='latin_1') as arquivo_contato:
        for linha in arquivo_contato:
            print(linha, end= '')
            
except FileNotFoundError:
    print('Arquivo não encontrado')
