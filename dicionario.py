dadosPessoais={'nome':'Hélio Augusto','idade':37,'telefone':'(86)9 99450-5802',
               'endereço':'Rua Riacheulo,1770 Vermelha CEP:64.018-060 Teresina-PI'}

print('\nNome:',dadosPessoais['nome'],
      '\nIdade:',dadosPessoais['idade'],
      '\nTelefone:',dadosPessoais['telefone'],
      '\nEndereço:',dadosPessoais['endereço'])

for dados in dadosPessoais:
    print (dados+'=',dadosPessoais[dados])
