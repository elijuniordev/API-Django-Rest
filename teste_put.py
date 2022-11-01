import requests

headers = {'Authorization': 'Token 89dd3339ec818b5a4ccc91fa7ba72eee1adfede4'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "O Nicolas agora é homem",
    "url": "http://testenicolashomem.com.br",
}

# Buscando o curso com ID 11
#curso = requests.get(f'{url_base_cursos}11/', headers=headers)
#print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}11/', headers=headers, data=curso_atualizado)

# Testando o código de status HTTP 201
assert resultado.status_code == 200

# Testando se o título do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == curso_atualizado['titulo']