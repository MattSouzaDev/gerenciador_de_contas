# Gerenciador de Contas

Este é um aplicativo de terminal para gerenciar **contas a pagar e a receber**.  
Permite adicionar contas, listar, marcar como pagas e visualizar totais diretamente no console com uma interface colorida usando a biblioteca **Rich**.

---

## Como executar a aplicação

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/gerenciador-contas.git
cd gerenciador-contas

2. Criar e ativar um ambiente virtual (opcional, mas recomendado)

Windows:

python -m venv venv
venv\Scripts\activate

Linux/macOS:

python3 -m venv venv
source venv/bin/activate

3. Instalar as dependências

pip install rich

4. Executar a aplicação

python main.py

ou, se estiver usando Linux/macOS:

python3 main.py

5. Interagir com o menu

Após executar, será exibido o menu principal:

1 - Adicionar contas
2 - Listar contas

Siga as instruções na tela para adicionar, listar e atualizar suas contas.

As informações são salvas no arquivo contas.csv na raiz do projeto.
Não é necessário criar o arquivo manualmente — ele será criado automaticamente ao adicionar a primeira conta.
    Requisitos

    Python 3.10 ou superior

    Biblioteca rich


