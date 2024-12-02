# Gerenciador de Usuários e Autenticação

Este repositório contém a implementação e os testes de um sistema básico de gerenciamento de usuários, incluindo funcionalidades de cadastro e login. O sistema permite o registro de usuários com validação de email e senha, e autenticação com login.

## Funcionalidades do Sistema

O sistema implementa as seguintes funcionalidades:

1. **Cadastro de Usuário**: Permite cadastrar um usuário com nome, email e senha.
   - O email deve ser único, ou seja, dois usuários não podem ter o mesmo email.
   - A senha deve ter pelo menos 8 caracteres e incluir pelo menos um número.

2. **Login de Usuário**: Permite que o usuário faça login com o email e senha cadastrados.
   - O sistema valida se o email e a senha estão corretos.

## Requisitos de Qualidade

Este projeto segue as melhores práticas de qualidade de software, com foco na robustez do sistema e na cobertura de testes. Os requisitos de qualidade incluem:

- **Cobertura de código**: Garantir que uma alta porcentagem do código seja coberta pelos testes automatizados.
- **Tempo de resposta**: O sistema deve ser eficiente e responder rapidamente durante as operações de cadastro e login.
- **Validação de dados**: O sistema deve validar corretamente todos os dados de entrada (email único e senha com requisitos de segurança).

## Estratégia de Testes

Para garantir que o sistema esteja funcionando corretamente e atenda aos requisitos de qualidade, uma estratégia de testes foi definida:

- **Testes de unidade**: Cada funcionalidade do sistema foi testada de forma isolada.
- **Testes de exceção**: O sistema lida corretamente com entradas inválidas e gera erros quando necessário.
- **Testes de limites**: Como senhas com menos de 8 caracteres ou emails duplicados.

### Testes Implementados

Os seguintes testes foram implementados utilizando o **pytest**:

- **Cadastro de Usuário**:
  - Teste de cadastro de usuário válido.
  - Teste de cadastro com email duplicado.
  - Teste de cadastro com senha curta.
  - Teste de cadastro com senha sem número.

- **Login de Usuário**:
  - Teste de login com credenciais válidas.
  - Teste de login com email não cadastrado.
  - Teste de login com senha incorreta.

- **Testes Adicionais**:
  - Teste de email com formato inválido.
  - Teste de senha com caracteres especiais.
  - Teste de email com o tamanho máximo.
  - Teste de concorrência com múltiplos cadastros simultâneos.

## Como Rodar os Testes

### Pré-requisitos

Certifique-se de ter o Python e o pytest instalados. Para instalar as dependências necessárias, execute:

```bash
pip install -r requirements.txt
