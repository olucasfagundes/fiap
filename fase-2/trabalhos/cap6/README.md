# SysAgro - MVP de Gestão Agrícola

Este projeto é um MVP (Produto Mínimo Viável) do sistema **SysAgro**, um exercicio para o capitulo 6 da fase 2 da FIAP, uma solução básica para gestão e controle agrícola, desenvolvida para centralizar e organizar dados essenciais do ciclo produtivo de uma safra.

## Objetivo

O SysAgro permite o registro e acompanhamento de informações fundamentais do processo agrícola, incluindo:

- Cadastro de propriedades, produtores, técnicos, produtos e insumos
- Registro de plantações e safras
- Controle de sensores instalados nas plantações e coleta de dados ambientais (umidade, pH, nutrientes, etc.)
- Associação de insumos aplicados a cada safra
- Geração de relatórios em formato JSON para análise de produção, uso de insumos e condições ambientais

## Funcionalidades

- **Inserção de dados**: Interface de linha de comando para cadastrar todas as entidades do sistema diretamente no banco de dados PostgreSQL.
- **Geração de relatórios**: Exportação de relatórios em JSON na pasta `relatorios/`, facilitando a análise e integração com outras ferramentas.
- **Estrutura modular**: Código organizado em módulos para facilitar manutenção e expansão futura.

## Estrutura do Projeto

- `src/classes/`: Definição das classes de domínio (entidades do sistema)
- `src/infra/`: Scripts de banco de dados (DDL, massa de testes) e conexão PostgreSQL
- `src/utils/`: Menus, inserção de dados e geração de relatórios
- `relatorios/`: Relatórios gerados em JSON
- `main.py`: Ponto de entrada do sistema

## Como usar

1. Configure o banco de dados PostgreSQL conforme o arquivo `src/infra/db.py`.
2. Execute os scripts de criação de tabelas (`src/infra/ddl.sql`) e de massa de testes (`src/infra/testes.sql`) se desejar dados de exemplo.
3. Instale as dependências (`pip install -r requirements.txt`).
4. Execute o sistema com `python main.py`.
5. Utilize os menus para inserir dados ou gerar relatórios.

## Observações

- Este MVP é uma base para projetos de agricultura digital, podendo ser expandido para incluir dashboards, APIs, automações e integrações com dispositivos IoT.
- O foco está na centralização e organização dos dados do ciclo produtivo agrícola, facilitando a gestão e a tomada de decisão.

---
Desenvolvido para fins acadêmicos e de prototipagem.
