CREATE TABLE productos(
id_productos INT AUTO_INCREMENT PRIMARY KEY,
NAME VARCHAR(200),
precio double,
descripcion VARCHAR(200),
marca VARCHAR(200)
);

CREATE TABLE categorias(
id_categorias INT AUTO_INCREMENT PRIMARY KEY,
NAME VARCHAR(200)
);

CREATE TABLE facturas(
id_facturas INT AUTO_INCREMENT PRIMARY KEY,
id_categorias INT,
id_productos INT,
cantidad INT,
FOREIGN KEY (id_productos) REFERENCES productos(id_productos),
FOREIGN KEY (id_categorias) REFERENCES categorias(id_categorias)
); 
