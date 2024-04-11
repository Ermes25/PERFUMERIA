class productos:
    def __init__(self, name, precio, descripcion, marca , id):
        self.name = name
        self.precio = precio
        self.descripcion = descripcion
        self.marca = marca
        self.id = id

    def __str__(self):
        return self.name
    def get_price(self):
        return self.precio
    
class categorias:
    def __init__(self,name,sexo,id):
        self.name = name
        self.sexo = sexo
        self.id = id
    
    def __str__(self):
        return self.name


class facturas:
    def __init__(self,id_categorias,id_productos,cantidad,id):
        self.id_categorias = id_categorias
        self.id_productos = id_productos
        self.cantidad = cantidad
        self.id = id

    def __str__(self):
        return self.name
    
    def get_products(self):
        return self.Productos.name    
    
    def get_categories(self):
        return self.categorias.name
    