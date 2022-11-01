import requests


class TestCursos:
    headers = {'Authorization': 'Token 89dd3339ec818b5a4ccc91fa7ba72eee1adfede4'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
    
    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)
        
        assert resposta.status_code == 200
        
    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}5/', headers=self.headers)
        
        assert resposta.status_code == 200
        
    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Programação com Ruby",
            "url": "http://cursoruby.com.br"
        }
        
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)
        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']
    
    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo curso de Ruby",
            "url": "http://novocursoruby.com.br"
        }
        
        resposta = requests.put(url=f'{self.url_base_cursos}12/', headers=self.headers, data=atualizado)
        assert resposta.status_code == 200
    
    def test_put_titulo_curso(self):
        atualizado2 = {
            "titulo": "Novo curso de Ruby2",
            "url": "http://novocursoruby2.com.br"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}12/', headers=self.headers, data=atualizado2)
        assert resposta.json()['titulo'] == novo['titulo']
        
    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}10/', headers=self.headers)
        assert resposta.status_code == 204 and len(resposta.text) == 0
        
