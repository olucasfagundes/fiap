-- Criação das tabelas conforme o DER e as classes Python

CREATE TABLE proprietario (
    id_proprietario VARCHAR PRIMARY KEY,
    nome VARCHAR NOT NULL,
    cpf VARCHAR NOT NULL,
    telefone VARCHAR,
    email VARCHAR
);

CREATE TABLE organizacao (
    id_organizacao VARCHAR PRIMARY KEY,
    nome VARCHAR NOT NULL,
    cnpj VARCHAR NOT NULL,
    id_proprietario VARCHAR NOT NULL REFERENCES proprietario(id_proprietario)
);

CREATE TABLE cadastro_tecnico (
    id_tecnico VARCHAR PRIMARY KEY,
    nome_completo VARCHAR NOT NULL,
    registro_crea VARCHAR,
    telefone VARCHAR,
    email VARCHAR,
    especialidade VARCHAR
);

CREATE TABLE produtor (
    id_produtor VARCHAR PRIMARY KEY,
    id_organizacao VARCHAR NOT NULL REFERENCES organizacao(id_organizacao),
    nome VARCHAR NOT NULL,
    cnpj VARCHAR,
    id_tecnico VARCHAR NOT NULL REFERENCES cadastro_tecnico(id_tecnico)
);

CREATE TABLE produto (
    id_produto VARCHAR PRIMARY KEY,
    id_produtor VARCHAR NOT NULL REFERENCES produtor(id_produtor),
    nome VARCHAR NOT NULL,
    tipo VARCHAR
);

CREATE TABLE plantacao (
    id_plantacao VARCHAR PRIMARY KEY,
    id_produto VARCHAR NOT NULL REFERENCES produto(id_produto),
    area_total_ha FLOAT,
    localizacao_gps VARCHAR
);

CREATE TABLE safra (
    id_safra VARCHAR PRIMARY KEY,
    id_plantacao VARCHAR NOT NULL REFERENCES plantacao(id_plantacao),
    ano INT,
    previsao_producao_kg FLOAT,
    producao_real_kg FLOAT
);

CREATE TABLE sensor (
    id_sensor VARCHAR PRIMARY KEY,
    id_safra VARCHAR NOT NULL REFERENCES safra(id_safra),
    tipo_sensor VARCHAR,
    status_operacional VARCHAR,
    fabricante VARCHAR,
    localizacao_gps VARCHAR
);

CREATE TABLE dado_coletado (
    id_dado VARCHAR PRIMARY KEY,
    id_sensor VARCHAR NOT NULL REFERENCES sensor(id_sensor),
    timestamp TIMESTAMP,
    valor FLOAT,
    unidade_medida VARCHAR,
    observacao VARCHAR
);

CREATE TABLE insumo (
    id_insumo VARCHAR PRIMARY KEY,
    nome VARCHAR NOT NULL,
    tipo VARCHAR,
    fornecedor VARCHAR,
    unidade_medida VARCHAR
);

CREATE TABLE safra_insumo (
    id_safra VARCHAR NOT NULL REFERENCES safra(id_safra),
    id_insumo VARCHAR NOT NULL REFERENCES insumo(id_insumo),
    quantidade FLOAT,
    PRIMARY KEY (id_safra, id_insumo)
);
