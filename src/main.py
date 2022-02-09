import contatos_utils

try:
    # contatos = contatos_utils.csv_para_contatos('src/data/contatos.csv')
    # contatos_utils.contato_para_pickle(contatos, 'src/data/contatos.p')

    #contatos = contatos_utils.pickle_para_contato('src/data/contatos.p')
    #contatos_utils.contatos_para_json(contatos, 'src/data/contatos.json')
    contatos = contatos_utils.json_para_contatos('src/data/contatos.json')
    
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')
except FileNotFoundError:
    print('Arquivo não encontrado')
