# Processamento de Dados Excel com Pandas

Este projeto automatiza o processamento de arquivos Excel (`.xlsx`) armazenados em `src/data/raw`, aplica transformações de dados usando **Pandas** e gera um arquivo consolidado em `src/data/ready/clean.xlsx`.

### Data Raw 
(Colocado apenas por que é um projeto para portifólio)
![image](https://github.com/user-attachments/assets/84859a86-c4c5-46fb-8232-f9f72af9f818)

### Data Ready (Pós ETL)
![image](https://github.com/user-attachments/assets/c2e5db34-bd91-4101-bb57-b7d97d556759)

---

## 🚀 Funcionalidades

* Busca todos os arquivos `.xlsx` em `src/data/raw`
* Lê cada arquivo utilizando **Pandas**
* Adiciona colunas auxiliares:

  * `location`: identifica o país a partir do nome do arquivo (`br`, `fr`, `it`)
  * `campaign`: extrai o parâmetro `utm_campaign` da URL (`utm_link`)
  * `data_da_venda`: converte datas de `MMDDYY` para `DD-MM-YY`
  * `FileName`: nome do arquivo de origem
* Remove a coluna de data original (`sale_date`)
* Consolida todos os DataFrames em um único arquivo Excel (`clean.xlsx`)
* Tratamento de erros para leitura de arquivos e ausência de arquivos de entrada

---

## 📁 Estrutura de Pastas

```
project-root/
├── Docs/
│   └── how-to.md
├── src/
│   ├── data/
│   │   ├── raw/      # arquivos .xlsx de entrada
│   │   └── ready/    # diretório de saída para clean.xlsx
│   └── scripts/
│       └── main.py   # script principal
├── .gitignore
├── poetry.lock
├── pyproject.toml     # config do Poetry
└── README.md
```

---

## ⚙️ Gerenciamento de Dependências com Poetry

Este projeto utiliza **Poetry** para gerenciar dependências e ambiente virtual.

### Instalação do Poetry

```bash
# Linux / macOS
curl -sSL https://install.python-poetry.org | python3 -
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### pyproject.toml (exemplo)

```toml
[tool.poetry]
name = "learn-python"
version = "0.1.0"
description = "Processamento de dados Excel com Pandas"
authors = ["K4L1B3 <luizhlimagomes28@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.9"
pandas = "^2.2.3"
openpyxl = "^3.1.5"
xlsxwriter = "^3.2.3"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

---

## 🔧 Como Executar

1. Clone o repositório e acesse a pasta do projeto:

   ```bash
   git clone <repo-url>
   cd project-root
   ```
2. Instale as dependências com Poetry:

   ```bash
   poetry install
   ```
3. Execute o script:

   ```bash
   poetry run python src/scripts/main.py
   ```

Ao concluir, o arquivo `clean.xlsx` será gerado em `src/data/ready/`.

---

## 🤝 Contribuições

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature:

   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas alterações:

   ```bash
   git commit -m "Adiciona nova feature"
   ```
4. Envie para o repositório remoto:

   ```bash
   git push origin minha-feature
   ```
5. Abra um pull request.

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

*Desenvolvido por Luiz Henrique*
