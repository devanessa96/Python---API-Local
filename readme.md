API de Gerenciamento de Imóveis

O sistema permite consultar, cadastrar, editar e remover imóveis, armazenando os dados em um arquivo JSON.

Objetivo:
- Treinar métodos HTTP com GET, POST, PUT e DELETE.
- GET para consulta de imóveis por ID ou lista geral.
- POST para cadastro de novos imóveis e condicionais de campos para não deixar informações vazias.
- PUT para atualização de informações de um imóvel com condicionais de campos para não deixar informações vazias.
- DELETE para remoção através do ID de cada imóvel.

Tecnologias Utilizadas:
- Python
- Biblioteca Flask
- JSON
- REST API
- Métodos HTTP (GET, POST, PUT, DELETE)

Ferramentas Utilizadas:
- VS Code
- Postman
- Terminal Linux Zorin OS

Estrutura do Projeto
crud/
│
├── app.py
├── dados.json
├── requirements.txt
└── README.md


Endpoints da API: 
- Listar todos os imóveis
GET /v1/imoveis
Retorna todos os imóveis cadastrados.

- Buscar imóvel por ID
GET /v1/imoveis/{id}
Retorna um imóvel específico.

- Cadastrar imóvel
POST /v1/imoveis/cadastro
Exemplo de JSON:
{
  "id": 3,
  "titulo": "Apartamento no centro",
  "preco": 450000,
  "quarto": 2,
  "banheiro": 1,
  "metro2": 70
}
- Atualizar imóvel
PUT /v1/imoveis/{id}
Atualiza apenas os campos enviados.

- Deletar imóvel
DELETE /v1/imoveis/{id}
Remove o imóvel do sistema.

Como Instalar e Executar o Projeto
- Clonar o repositório
git clone https://github.com/devanessa96/CRUD-SIMPLES---IMOBILIARIA

Entrar na pasta do projeto:
cd crud
- Criar ambiente virtual:
python3 -m venv .venv

- Ativar o ambiente virtual
Linux/Mac:
source .venv/bin/activate
Windows:
.venv\Scripts\activate

- Instalar dependências
pip install -r requirements.txt

- Executar a aplicação
python app.py

O servidor iniciará em:
http://localhost:6000

- Exemplo de Uso
Consultar todos os imóveis pelo Postman:
http://localhost:6000/v1/imoveis

Consultar imóvel por ID:
http://localhost:6000/v1/imoveis/1
