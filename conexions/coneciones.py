import mysql.connector

class conexion:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None
        self.connect()

    def connect(self):
        self.cnx = mysql.connector.connect(user= self.user,password =self.password, host = self.host,database=self.database )

    def close(self):
        self.cnx.close()

    def execute_query(self, query, params):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        self.cnx.commit()
        cursor.close()
        return cursor

    def execute_read_query(self, query, params):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result

class con_pro:
    def __init__(self,conexion):
        self.conexion = conexion

    def get_all(self):
        query = 'SELECT * FROM productos'
        return self.conexion.execute_read_query(query,())
    
    def get_by_id(self):
        query = 'SELECT * FROM productos WHERE id = %s'
        return self.conexion.execute_read_query(query,(id,))

    def insert(self,productos):
        query = 'INSERT INTO productos(name,precio,descripcion,marca) values(%s, %s, %s, %s)'
        return self.conexion.execute_query(query,(productos.name,productos.precio,productos.descripcion,productos.marca))
    
    def update(self,productos):
        query = 'UPDATE productos SET name = %s, precio = %s, descripcion = %s , marca = %s WHERE id = %s'
        return self.conexion.execute_query(query,(productos.name, productos.precio,productos.descripcion,productos.marca,productos.id))

    def delete(self, id):
        query = 'DELETE FROM productos WHERE id = %s'
        return self.conexion.execute_query(query, (id,))

class con_cat:
    def __init__(self,conexion):
        self.conexion = conexion

    def get_all(self):
        query = 'SELECT * FROM categorias'
        return self.conexion.execute_read_query(query,())

    def get_by_id(self,id):
        query = 'SELECT * FROM categorias WHERE id = %s'
        return self.conexion.execute_read_query(query,(id,))

    def insert(self,categorias):
        query = 'INSERT INTO categorias (name,sexo) VALUES (%s,%s)'
        return self.conexion.execute_query(query,(categorias.name,categorias.sexo))

    def update(self,categorias):
        query = 'UPDATE categorias SET name = %s WHERE id = %s'
        return self.conexion.execute_query(query,(categorias.name,categorias.id))

    def delete(self,categorias):
        query = 'DELETE FROM categorias WHERE id = %s'
        return self.conexion.execute_query(query, (id,))

class con_fact:
    def __init__(self,conexion):
        self.conexion = conexion

    def get_all(self):
        query = 'SELECT * FROM facturas'
        return self.conexion.execute_read_query(query,())
    
    def get_by_id(self,id):
        query = 'SELECT * FROM facturas WHERE id = %s'
        return self.conexion.execute_read_query(query,(id,))

    def insert(self,facturas):
        query = 'INSERT INTO facturas (id_categorias,id_productos,cantidad) VALUES (%s,%s,%s)'
        return self.conexion.execute_query(query,(facturas.id_categorias,facturas.id_productos,facturas.cantidad))

    def update(self,facturas):
        query = 'UPDATE facturas SET id_categorias = %s, id_productos = %s, cantidad = %s WHERE id = %s'
        return self.conexion.execute_query(query, (facturas.id_categorias,facturas.id_productos,facturas.id))

    def delete(self,facturas):
        query = 'DELETE FROM facturas WHERE id = %s'
        return self.conexion.execute_query(query,(id,))