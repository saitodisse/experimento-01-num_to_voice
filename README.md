# Conversor de Números por Extenso

Este projeto é uma API desenvolvida com FastAPI que converte números inteiros em
sua forma por extenso em português. A aplicação também inclui uma interface web
simples para interação.

## Requisitos

- Python 3.12.2
- pip

## Instalação

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` com as seguintes variáveis:
   ```
   PORT=8000
   ```

## Execução

1. Execute a aplicação:
   ```bash
   python api.py
   ```

2. Acesse a aplicação em seu navegador:
   ```
   http://localhost:8000
   ```

## Deploy na Railway

1. Faça login na Railway e crie um novo projeto.
2. Conecte o repositório do GitHub ao projeto.
3. A Railway irá automaticamente detectar o `Procfile` e iniciar a aplicação.

## Uso

- Acesse a interface web para converter números por extenso.
- Use o endpoint `/converter/{numero}` para obter a conversão via API.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais
detalhes.
