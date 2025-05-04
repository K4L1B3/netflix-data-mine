# How To

Este guia rápido mostra como configurar o ambiente, instalar dependências e executar o projeto.

## 1. Pré-requisitos

* **Python 3.9+** instalado
* **Git** instalado (para clonar o repositório)
* **Poetry** instalado (gerenciador de dependências)

## 2. Instalar o Poetry

### Linux / macOS

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Windows (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Após a instalação, verifique:

```bash
poetry --version
```

## 3. Clonar o repositório

```bash
git clone <URL_DO_REPOSITÓRIO>
cd project-root
```

## 4. Instalar dependências

Dentro da raiz do projeto, execute:

```bash
poetry install
```

Isso criará um ambiente virtual isolado e instalará todas as dependências listadas em `pyproject.toml`.

## 5. Executar o script principal

Ainda na raiz do projeto, execute:

```bash
poetry run python src/scripts/main.py
```

* O script lerá todos os arquivos `*.xlsx` em `src/data/raw`
* Processará e consolidará os dados
* Gerará `clean.xlsx` em `src/data/ready/`

## 6. Acessar o resultado

* Abra o arquivo `src/data/ready/clean.xlsx` em seu editor de planilhas preferido para visualizar os dados consolidados.

---

## 7. Gerenciando a versão do Python com Poetry

Em alguns casos, o Poetry pode usar uma versão diferente de Python (por exemplo, 3.8) e gerar um fallback para 3.9 automaticamente. Para controlar isso explicitamente:

1. Garanta que o Python 3.9 esteja instalado no sistema e acessível via `python3.9` ou caminho absoluto.
2. Aponte o Poetry para usar essa versão:

   ```bash
   # Usando o alias no PATH:
   poetry env use python3.9

   # Ou especificando o executável completo:
   poetry env use /usr/bin/python3.9
   ```
3. Verifique o ambiente ativo e a versão do Python:

   ```bash
   poetry env info
   ```
4. (Opcional) Ative o shell do Poetry para não precisar usar `poetry run`:

   ```bash
   poetry shell
   ```
5. Execute o script no caminho correto (lembre-se: `main.py` está em `src/scripts/`):

   ```bash
   # Sem shell:
   poetry run python src/scripts/main.py

   # Com shell ativado:
   python src/scripts/main.py
   ```

Pronto! Agora o Poetry usará sempre a versão desejada de Python e você saberá exatamente como rodar o script.
