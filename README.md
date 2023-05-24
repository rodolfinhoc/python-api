# API em Python com Banco de Dados MySQL

Este repositório contém uma API básica em Python que utiliza o framework Flask para criar um servidor web e se comunica com um banco de dados MySQL. Abaixo, você encontrará instruções passo a passo para configurar, instalar e implementar essa API.

## Pré-requisitos

Antes de prosseguir, certifique-se de ter os seguintes pré-requisitos instalados em sua máquina:

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- pip (gerenciador de pacotes do Python): [Instalando o pip](https://pip.pypa.io/en/stable/installation/)

## Passo 1: Configuração do Banco de Dados MySQL

1. Acesse o site [https://www.freemysqlhosting.net/](https://www.freemysqlhosting.net/) e crie uma conta gratuita.
2. Após criar a conta, você receberá as informações de acesso ao banco de dados, incluindo o nome do host, nome de usuário, senha e nome do banco de dados.
3. Anote essas informações, pois você precisará delas posteriormente.

## Passo 2: Configuração do Ambiente Virtual

1. Crie um ambiente virtual para isolar as dependências do projeto. Abra o terminal e execute o seguinte comando:

   ```bash
   python3 -m venv nome-do-ambiente-virtual
   ```

2. Ative o ambiente virtual. No Windows, execute:

   ```bash
   nome-do-ambiente-virtual\Scripts\activate
   ```

   No macOS/Linux, execute:

   ```bash
   source nome-do-ambiente-virtual/bin/activate
   ```

## Passo 3: Instalação das Dependências

1. Navegue até o diretório raiz do projeto no terminal.
2. Instale as dependências executando o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

## Passo 4: Configuração da API

1. Abra o arquivo `app.py` no editor de texto de sua preferência.
2. No trecho abaixo, atualize as configurações do MySQL de acordo com as informações fornecidas pelo site freemysqlhosting.net:

   ```python
   app.config['MYSQL_HOST'] = 'sql10.freemysqlhosting.net'
   app.config['MYSQL_USER'] = 'sql10620819'
   app.config['MYSQL_PASSWORD'] = 'W4R29qXrxQ'
   app.config['MYSQL_DB'] = 'sql10620819'
   ```

3. Certifique-se de que o valor da chave `JWT_SECRET_KEY` seja único e seguro. Caso deseje gerar uma chave aleatória, você pode usar ferramentas online ou o seguinte comando Python:

   ```python
   import secrets

   print(secrets.token_hex(16))
   ```

   Copie o valor gerado e cole-o como o novo valor da chave `JWT_SECRET_KEY`.

## Passo 5: Executando a API

1. Certifique-se de estar no diretório raiz do projeto no terminal.
2. Execute o seguinte comando para iniciar o servidor da API:

   ```bash
   python app.py
   ```

   O servidor será iniciado e estará pronto para receber solicitações na porta 5000.

## Uso da API

A API possui as seguintes rotas:

- `/`: Rota inicial, renderiza

 o arquivo `index.html`.
- `/login`: Rota para autenticação. Aceita uma solicitação HTTP POST com os campos "usuario" e "senha". Retorna um token de acesso JWT válido se as credenciais forem válidas.
- `/protected`: Rota protegida que requer autenticação. Apenas solicitações HTTP GET são permitidas nesta rota.
