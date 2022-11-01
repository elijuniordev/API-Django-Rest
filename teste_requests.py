import requests

# GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP
#print(avaliacoes.status_code)

# Acessando os dados da resposta
#print(avaliacoes.json())
# print(type(avaliacoes.json())) # O resultado é um dicionário

# Acessando a quantidade de registros
#print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
#print(avaliacoes.json()['next'])

# Acessando os resultados desta página
#print(avaliacoes.json()['results'])

# Acessar o primeiro elemento da lista de resultados
#print(avaliacoes.json()['results'][0])

# Acessar o último elemento da lista de resultados
#print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da pessoa que fez a ultima avaliação
# print(avaliacoes.json()['results'][-1]['nome'])

# GET Avaliação
#avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/7/')
# print(avaliacao.json())

########################################

# GET Cursos

headers = {'Authorization': 'Token 89dd3339ec818b5a4ccc91fa7ba72eee1adfede4'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())



