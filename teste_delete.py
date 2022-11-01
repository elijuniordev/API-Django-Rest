import requests

headers = {'Authorization': 'Token 89dd3339ec818b5a4ccc91fa7ba72eee1adfede4'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}11/', headers=headers)

# Testando o código de status HTTP 204
assert resultado.status_code == 204

# Testando se o tamanho do conteudo retornado é 0
assert len(resultado.text) == 0