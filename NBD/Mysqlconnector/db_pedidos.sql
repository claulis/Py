CREATE DATABASE db_pedidos;
use db_pedidos;

CREATE TABLE pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(100),
    data_pedido DATE
);

CREATE TABLE item_pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    produto VARCHAR(100),
    quantidade INT,
    preco DECIMAL(10,2),
    FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);
