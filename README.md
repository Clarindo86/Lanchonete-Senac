 Lanchonete SENAC

 Sobre o projeto

Este projeto foi desenvolvido como atividade do curso do SENAC.

A ideia é criar um sistema para organizar o cardápio de uma lanchonete. Com ele, podemos cadastrar categorias, cadastrar produtos e consultar as informações dos produtos.

Também fiz uma integração com o IBGE para consultar os estados e os municípios do Brasil.

 O que o sistema faz

 Cadastra categorias.
 Cadastra produtos.
 Consulta, altera e exclui informações.
  Mostra a categoria de cada produto.
 Permite pesquisar produtos pelo nome.
 Permite filtrar produtos disponíveis e indisponíveis.
 Permite buscar produtos por categoria.
 Divide os resultados em páginas.
 Utiliza token para controlar o acesso às operações.
 Consulta estados e municípios pela API do IBGE.
 Mostra a documentação da API pelo Swagger.

Ferramentas utilizadas

 Python: linguagem utilizada no projeto.
 Django: ferramenta utilizada para desenvolver o sistema.
 Django REST Framework: utilizado para criar a API.
 SQLite: banco de dados do projeto.
 Requests: utilizado para buscar informações no IBGE.
 Postman: ferramenta para fazer testes na API.
 Swagger: utilizado para visualizar a documentação da API.

 Organização das pastas

cardapio`: contém os arquivos de categorias, produtos e suas funcionalidades.
 lanchonete`: contém as configurações principais do projeto.
 manage.py`: arquivo utilizado para executar comandos do Django.
 db.sqlite3`: banco de dados.
 requirements.txt`: lista das bibliotecas utilizadas.
 `README.md`: arquivo com as informações do projeto.

## Como executar o projeto

Primeiro, abra o CMD ou o terminal do VS Code dentro da pasta do projeto.

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual:

```bash
venv\Scripts\activate
```

Instale as bibliotecas:

```bash
pip install -r requirements.txt
```

Prepare o banco de dados:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

Depois, abra o navegador e acesse:

`http://127.0.0.1:8000/`

## Endereços da API

Com o servidor funcionando, podemos acessar:

| Funcionalidade | Endereço |
|---|---|
| Categorias | `/api/categorias/` |
| Produtos | `/api/produtos/` |
| Estados do IBGE | `/api/ibge/estados/` |
| Municípios de Pernambuco | `/api/ibge/estados/26/municipios/` |
| Autenticação por token | `/api/token/` |

Também podemos pesquisar e filtrar produtos:

- `?search=hamburguer` para pesquisar pelo nome.
- `?disponivel=true` para mostrar produtos disponíveis.
- `?disponivel=false` para mostrar produtos indisponíveis.
- `?categoria=1` para buscar produtos de uma categoria.
- `?page=2` para acessar a segunda página.

Podemos também combinar os filtros.

## Autenticação

O sistema utiliza token para controlar o acesso às operações que precisam de autenticação.

Para conseguir um token, é necessário informar um usuário e uma senha cadastrados no sistema.

## Documentação da API

A documentação pode ser acessada pelo navegador:

Swagger:

`http://127.0.0.1:8000/api/docs/`

ReDoc:

`http://127.0.0.1:8000/api/redoc/`

Nessas páginas podemos visualizar os endereços e as funcionalidades da API.

## Integração com o IBGE

Também desenvolvi uma parte do sistema que busca informações diretamente na API do IBGE.

Com essa integração, conseguimos consultar os estados brasileiros e os municípios de cada estado.

Para isso, utilizei a biblioteca Requests do Python.

## Testes e validações

Criei algumas regras para evitar informações incorretas, como nomes vazios e preços negativos.

Também desenvolvi testes automáticos para verificar se essas funcionalidades estão funcionando.

Na última execução, os sete testes foram aprovados.

Para executar os testes novamente, basta utilizar:

```bash
python manage.py test cardapio
```

## Finalização

O projeto foi desenvolvido por etapas. Fui criando as funcionalidades, verificando o funcionamento e corrigindo os problemas que apareceram durante o desenvolvimento.

Com esse trabalho, pude praticar Python, Django, criação de APIs, banco de dados e integração com serviços externos.
