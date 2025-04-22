# Sistema de Monitoramento Agrícola - FarmTech Solutions

## Introdução

Este documento descreve a estrutura de banco de dados desenvolvida pela equipe de desenvolvedores da Startup FarmTech Solutions para o sistema de monitoramento agrícola baseado em sensores IoT.

O sistema foi projetado para atender produtores rurais que utilizam sensoriamento em suas plantações para aplicação precisa de água e nutrientes, visando otimizar a produção através da agricultura digital.

## Problema e Contexto

Um produtor rural utiliza sensoriamento em sua plantação para aplicar a quantidade precisa de água e vitaminas necessárias para aumentar a produção. Três tipos principais de sensores são utilizados:

- **S1**: Sensor de umidade do solo
- **S2**: Sensor de pH do solo
- **S3**: Sensor de nutrientes - fósforo (P) e potássio (K) do NPK

O sistema precisa:
1. Monitorar continuamente diferentes culturas
2. Coletar e processar dados em tempo real
3. Sugerir ajustes na irrigação e aplicação de nutrientes
4. Prever necessidades futuras com base em dados históricos
5. Otimizar o uso de recursos (água e insumos)

## Requisitos de Informações

Para atender às necessidades do produtor rural, identificamos as seguintes informações relevantes:

1. **Monitoramento de Irrigação**:
   - Quantidade total de água aplicada por período (dia/semana/mês)
   - Histórico de ajustes na irrigação
   - Relação entre umidade do solo e aplicação de água

2. **Análise de Solo**:
   - Variação do pH do solo ao longo do tempo
   - Níveis de nutrientes (P, K) em diferentes áreas da plantação
   - Correlação entre pH e níveis de nutrientes

3. **Gestão de Culturas**:
   - Desempenho de diferentes culturas sob as mesmas condições
   - Necessidades específicas de cada tipo de cultura
   - Produtividade por safra

4. **Previsão e Otimização**:
   - Previsões de necessidades futuras de irrigação
   - Recomendações para aplicação de nutrientes
   - Análise de eficiência dos recursos aplicados

## Modelagem de Dados

Para atender a estes requisitos, desenvolvemos um Modelo Entidade-Relacionamento (MER) que estrutura o armazenamento e análise dos dados coletados pelos sensores.

### Entidades e Atributos Principais

Nossa solução inclui entidades para representar organizações, produtores, produtos agrícolas, plantações, safras, sensores e dados coletados. Cada entidade possui atributos específicos que capturam as informações necessárias para análise e tomada de decisão.

### Relacionamentos e Cardinalidade

O modelo estabelece relacionamentos precisos entre as entidades, respeitando as regras de negócio e as necessidades de informação. Por exemplo, a relação entre sensores e dados coletados é de um-para-muitos, permitindo o armazenamento do histórico completo de leituras de cada sensor.

### Tipos de Dados

Cada atributo foi cuidadosamente tipificado para garantir o armazenamento adequado das informações:
- Identificadores: strings para flexibilidade
- Medições: valores numéricos (float) para precisão
- Datas e horários: formato datetime para análise temporal
- Texto: varchar para nomes e descrições
- Coordenadas GPS: formato string para localização precisa

## Entidades Principais

1. **ORGANIZACAO** - Representa a empresa ou organização agrícola
2. **PROPRIETARIO** - Pessoa responsável pela organização agrícola
3. **PRODUTOR** - Produtor rural vinculado a uma organização
4. **CADASTRO_TECNICO** - Profissional técnico que assiste o produtor
5. **PRODUTO** - Tipo de cultura agrícola cultivada (soja, milho, etc.)
6. **PLANTACAO** - Área específica destinada ao cultivo de um produto
7. **SAFRA** - Ciclo de produção de uma plantação em um período específico
8. **SENSOR** - Dispositivo IoT que monitora condições da plantação (umidade, pH, nutrientes)
9. **DADO_COLETADO** - Registro individual de leitura de um sensor
10. **INSUMO** - Produto aplicado na plantação (fertilizantes, defensivos)
11. **SAFRA_INSUMO** - Associação entre insumos aplicados e safras específicas

## Relacionamentos

- **ORGANIZACAO-PROPRIETARIO**: Uma organização pertence a exatamente um proprietário (1:1)
- **ORGANIZACAO-PRODUTOR**: Uma organização pode possuir vários produtores (1:N)
- **PRODUTOR-CADASTRO_TECNICO**: Um produtor é assistido por um técnico (1:1)
- **PRODUTOR-PRODUTO**: Um produtor pode cultivar vários tipos de produtos (1:N)
- **PRODUTO-PLANTACAO**: Um produto pode ter várias plantações (1:N)
- **PLANTACAO-SAFRA**: Uma plantação pode gerar várias safras ao longo do tempo (1:N)
- **SAFRA-SENSOR**: Uma safra pode utilizar vários sensores para monitoramento (1:N)
- **SENSOR-DADO_COLETADO**: Um sensor coleta múltiplos dados ao longo do tempo (1:N)
- **SAFRA-SAFRA_INSUMO**: Uma safra pode utilizar vários insumos (1:N)
- **INSUMO-SAFRA_INSUMO**: Um insumo pode ser aplicado em várias safras (1:N)

## Diagrama Entidade-Relacionamento (DER)

O Diagrama Entidade-Relacionamento completo pode ser encontrado em [diagrama_der.md](diagrama_der.md). Este diagrama visual representa todas as entidades, atributos e relacionamentos do sistema, facilitando a compreensão da estrutura do banco de dados.

erDiagram
    ORGANIZACAO ||--|| PROPRIETARIO : pertence
    ORGANIZACAO ||--o{ PRODUTOR : possui
    PRODUTOR ||--|| CADASTRO_TECNICO : possui
    PRODUTOR ||--o{ PRODUTO : cultiva
    PRODUTO ||--o{ PLANTACAO : possui
    PLANTACAO ||--o{ SAFRA : gera
    SAFRA ||--o{ SENSOR : usa
    SENSOR ||--o{ DADO_COLETADO : gera
    SAFRA ||--o{ SAFRA_INSUMO : possui
    INSUMO ||--o{ SAFRA_INSUMO : compoe

    ORGANIZACAO {
        string id_organizacao PK
        string nome
        string cnpj
        string id_proprietario FK
    }

    PROPRIETARIO {
        string id_proprietario PK
        string nome
        string cpf
        string telefone
        string email
    }

    PRODUTOR {
        string id_produtor PK
        string id_organizacao FK
        string nome
        string cnpj
        string id_tecnico FK
    }

    CADASTRO_TECNICO {
        string id_tecnico PK
        string nome_completo
        string registro_crea
        string telefone
        string email
        string especialidade
    }

    PRODUTO {
        string id_produto PK
        string id_produtor FK
        string nome
        string tipo
    }

    PLANTACAO {
        string id_plantacao PK
        string id_produto FK
        float area_total_ha
        string localizacao_gps
    }

    SAFRA {
        string id_safra PK
        string id_plantacao FK
        int ano
        float previsao_producao_kg
        float producao_real_kg
    }

    SENSOR {
        string id_sensor PK
        string id_safra FK
        string tipo_sensor
        string status_operacional
        string fabricante
        string localizacao_gps
    }

    DADO_COLETADO {
        string id_dado PK
        string id_sensor FK
        datetime timestamp
        float valor
        string unidade_medida
        string observacao
    }

    INSUMO {
        string id_insumo PK
        string nome
        string tipo
        string fornecedor
        string unidade_medida
    }

    SAFRA_INSUMO {
        string id_safra FK
        string id_insumo FK
        float quantidade
    }

## Conclusão

O modelo de dados desenvolvido permite o armazenamento eficiente dos dados coletados pelos sensores, possibilitando análises detalhadas e recomendações precisas para o produtor rural. A estrutura é flexível e escalável, podendo ser adaptada para diferentes culturas e condições, sempre mantendo o foco na otimização dos recursos e maximização da produtividade.

A implementação deste modelo de dados é fundamental para o sucesso do sistema de monitoramento agrícola da FarmTech Solutions, permitindo transformar dados brutos de sensores em informações acionáveis para o produtor rural.
