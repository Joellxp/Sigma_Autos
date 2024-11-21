create database connectsigma;
use connectsigma;

CREATE TABLE clientes (
    cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco_bairro VARCHAR(50),
    endereco_cidade VARCHAR(50),
    endereco_estado CHAR(2),
    telefone_residencial VARCHAR(15),
    celular VARCHAR(15),
    renda DECIMAL(10, 2)
);

CREATE TABLE vendedores (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL
);

CREATE TABLE veiculos (
    numero_chassi VARCHAR(17) PRIMARY KEY,
    placa VARCHAR(7),
    marca VARCHAR(50),
    modelo VARCHAR(50),
    ano_fabricacao INT,
    ano_modelo INT,
    cor VARCHAR(30),
    valor DECIMAL(10, 2)
);

CREATE TABLE operacoes_compra (
    numero INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    cliente_cpf VARCHAR(11) NOT NULL,
    vendedor_codigo INT NOT NULL,
    veiculo_chassi VARCHAR(17) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (cliente_cpf) REFERENCES clientes(cpf),
    FOREIGN KEY (vendedor_codigo) REFERENCES vendedores(codigo),
    FOREIGN KEY (veiculo_chassi) REFERENCES veiculos(numero_chassi)
);

CREATE TABLE operacoes_venda (
    numero INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    cliente_cpf VARCHAR(11) NOT NULL,
    vendedor_codigo INT NOT NULL,
    veiculo_chassi VARCHAR(17) NOT NULL,
    valor_entrada DECIMAL(10, 2),
    valor_financiado DECIMAL(10, 2),
    valor_total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (cliente_cpf) REFERENCES clientes(cpf),
    FOREIGN KEY (vendedor_codigo) REFERENCES vendedores(codigo),
    FOREIGN KEY (veiculo_chassi) REFERENCES veiculos(numero_chassi)
);

CREATE TABLE pedidos (
    numero INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    cliente_cpf VARCHAR(11) NOT NULL,
    vendedor_codigo INT NOT NULL,
    montadora_id INT NOT NULL,
    modelo VARCHAR(50),
    ano INT,
    cor VARCHAR(30),
    acessorios VARCHAR(255),
    valor DECIMAL(10, 2),
    FOREIGN KEY (cliente_cpf) REFERENCES clientes(cpf),
    FOREIGN KEY (vendedor_codigo) REFERENCES vendedores(codigo)
);

CREATE TABLE montadoras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cnpj VARCHAR(14) NOT NULL,
    razao_social VARCHAR(100),
    marca VARCHAR(50),
    contato VARCHAR(50),
    telefone_comercial VARCHAR(15),
    celular VARCHAR(15)
);

SELECT * FROM clientes ORDER BY nome;

SELECT * FROM veiculos ORDER BY marca, modelo;

