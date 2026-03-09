# Desafio MBA Engenharia de Software com IA - Full Cycle

## Iniciando Projeto

### Instalando python

- Caso não tenha o python instalado execute os comandos abaixo

#### Windows

```cmd
winget install Python.Python.3
ou
choco install python

python --version
pip --version
```

#### Linux

```cmd
sudo apt update

sudo apt install python3

sudo apt install python3-pip

python3 --version
```

#### Mac

```cmd
brew install python

python3 --version
```

### Instalando dependências

- Crie e ative um ambiente virtual antes de instalar as dependências

```cmd
python3 -m venv venv

source venv/bin/activate  # On macOS/Linux

venv\Scripts\activate     # On Windows
```

- Instalando as dependências:

```cmd
pip install -r requirements.txt
```

### Criando arquivo .env

- Renomei o arquivo .env.example para .env ou crie um novo arquivo .env

- Pode utilizar as envs já existentes para o banco de dados e sua url connection

- Caso queira mudar o nome da collection, só precisa alterar o nome no arquivo .env

### Api Keys

- Gere a sua api key na sua LLM de preferência, openapi ou google gemini.
- Adicione a api key gerada no seu .env, apenas a api key que realmente for usar, não adicione as duas

### Subindo banco de dados

- Instale o docker
- Rode o comando abaixo

```cmd
docker compose up -d
```

## Execução do Projeto

### Ingestão do PDF

- Executar ingestão do PDF

```cmd
python src/ingest.py
```

### Execução do chat

```cmd
python src/chat.py
```

- Faça sua pergunta via cli
- Aguarde a resposta
