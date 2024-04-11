import os
import sys
sys.path.append(r"C:\Users\ermes\OneDrive\Documentos\exfinal\perfum")
from conexions import coneciones
from models import clases as y

os.system('cls')

conex = coneciones.conexion("localhost","root","","perfumeria")
conex.connect()

def insertpro():
    os.system("cls")
    nombre = input("ingrese el Nombre del producto")
    price = float(input("Ingrese el precio del producto"))
    descrip = input("Ingrese una descripcion del producto")
    mark = input("INGRESE QUE TIPO DE MARCA ES")
    products = y.productos(nombre,price,descrip,mark,any)
    compra_pro = coneciones.con_pro(conex)
    compra_pro.insert(products)

def showpro():
    compra_pro = coneciones.con_pro(conex)
    products = compra_pro.get_all()
    for productos in products:
        print(productos)

def eliminarpro():
    os.system("")
    ep = input("ingresa el id de producto que deseas eliminar")
    compra_pro = coneciones.con_pro(conex)
    compra_pro.delete(ep)

def editar_pro():
    os.system("cls")
    ip_old = int(input("ingrese el id que desea actualizar"))
    ip_nombreN = input("ingrese el nuevo nombre del producto")
    ip_priceN = float(input("Ingresa el nuevo precio del producto"))
    ip_descripN = input("Ingresa su nueva descripcion")
    ip_MarcaN = input("Ingresa su nueva marca")
    compra_pro = coneciones.con_pro(conex)
    products = y.productos(ip_nombreN,ip_priceN,ip_descripN,ip_MarcaN,ip_old)
    compra_pro.update(products)
def searchpro():
    os.system("cls")
    isp = input("Ingresa el id que desea buscar")
    compro = coneciones.con_pro(conex)
    products = compro.get_by_id(isp)
    print(products)

def main_productos():
    opcion_pro = 0
    while(opcion_pro !=6):
        menu_productos()
        opcion_pro = int(input("Ingresa tu opcion"))
        if(opcion_pro == 1):
            insertpro()
            os.system("pause")
        if(opcion_pro == 2):
            showpro()
            os.system("pause")
        if(opcion_pro == 3):
            eliminarpro()
            os.system("pause")
        if(opcion_pro == 4):
            editar_pro()
            os.system("pause")
        if(opcion_pro == 5):
            searchpro()
            os.system("pause")
def menu_productos():
    print("1. Ingresa la Productos")
    print("2. Mostrar Productos")
    print("3. Eliminar Productos")
    print("4. Editar Productos")
    print("5. Buscar Productos")
    print("6. Salir")

def insertcat():
    os.system("cls")
    nombre = input("ingrese el nombre de la categoria")
    sexo = input("ingresa el sexo M o F")
    categories = y.categorias(nombre,sexo,any)
    compra_cat = coneciones.con_cat(conex)
    compra_cat.insert(categories)

def showcat():
    os.system("cls")
    compra_cat = coneciones.con_cat(conex)
    categories = compra_cat.get_all()
    for categoria in categories:
        print(categoria)
def  eliminarcat():
    os.system("cls")
    ec = input("elija el id de la categoria que desea eliminar") 
    compra_cat = coneciones.con_cat(conex)
    compra_cat.delete(ec)
def editar_cat():
    os.system("cls")
    showcat()
    oic = int(input("Ingrese el id que desea actualizar"))
    ic_nameN = input("Ingrese el nuevo nombre de la categoria")
    ic_sexoN = input("ingrese el nuevo sexo de la categoria")
    compra_cat = coneciones.con_cat(conex)
    categories = y.categorias(ic_nameN,ic_sexoN,oic)
    compra_cat.update(categories)
def searchcat():
    os.system("cls")
    isc = input("dime el id que deseas buscar")
    compra_cat = coneciones.con_cat(conex)
    compro = compra_cat.get_by_id(isc)
    print(compro)
def main_categorias():
    opcion_cat = 0
    while(opcion_cat !=6):
        menu_categorias()
        opcion_cat = int(input("Ingresa tu opcion"))
        if(opcion_cat == 1):
            insertcat()
            os.system("pause")
        if(opcion_cat == 2):
            showcat()
            os.system("pause")
        if(opcion_cat == 3):
            eliminarcat()
            os.system("pause")
        if(opcion_cat == 4):
            editar_cat()
            os.system("pause")
        if(opcion_cat == 5):
            searchcat()
            os.system("pause")
def menu_categorias():
    print("1. Ingresa la categoria")
    print("2. Mostrar categoria")
    print("3. Eliminar categoria")
    print("4. Editar categoria")
    print("5. Buscar categoria")
    print("6. Salir")
def insertfact():
    os.system("cls")
    idcat = showcat()
    idcat = int(input("elige una id de categoria para el producto"))
    idpro = showpro()
    idpro = int(input("elige una id de producto para la factura"))
    cantidad = int(input("ingrese una cantidad en la factura"))
    check = y.facturas(idcat,idpro,cantidad,any)
    compra_fact = coneciones.con_fact(conex)
    compra_fact.insert(check)
def showfact():
    compra_fact = coneciones.con_fact(conex)
    facturas = compra_fact.get_all()
    for factures in facturas:
        print(factures)
def eliminarfact():
    os.system("cls")
    efc = input("ingresa el id que deseas eliminar")
    compra_fact = coneciones.con_fact(conex)
    compra_fact.delete(efc)
def editar_fact():
    os.system("cls")
    showfact()
    ifo = int(input("elige el id que deseas editar"))
    if_ic = showcat()
    if_ic = int(input("ingrese el nuevo id que desea usar"))
    if_ip = showpro()
    if_ip = int(input("Elige nuevo id de producto"))
    co = int(input("ingrese la nueva cantidad"))
    compra_fact = coneciones.con_fact(conex)
    factures = y.facturas(if_ic,if_ip,co,ifo)
    compra_fact.update(factures)
def searchfact():
    os.system("cls")
    isf = input("elija el id que desea buscar")
    compra_fact = coneciones.con_fact(conex)
    factures = compra_fact.get_by_id(isf)
    print(factures)

def main_factura():
    opcion_fact = 0
    while(opcion_fact != 6):
        menu_factura()
        opcion_fact = int(input("Ingresa tu opcion"))
        if(opcion_fact == 1):
            insertfact()
            os.system("pause")
        if(opcion_fact == 2):
            showfact()
            os.system("pause")
        if(opcion_fact == 3):
            eliminarfact()
            os.system("pause")
        if(opcion_fact == 4):
            editar_fact()
            os.system("pause")
        if(opcion_fact == 5):
            searchfact()
            os.system("pause")
def menu_factura():
    print("1. Ingresa la factura")
    print("2. Mostrar facturas")
    print("3. Eliminar factura")
    print("4. Editar facturas")
    print("5. Buscar facturas")
    print("6. Salir")
def main():
    opcion_perfumes = 0
    while(opcion_perfumes != 3):
        print("1. MENU PRODUCTOS")
        print("2. MENU CATEGORIAS")
        print("3. MENU FACTURAS")
        opcion_perfumes = int(input("ELIGE UN MENU :"))
        if(opcion_perfumes == 1):
            main_productos()
            os.system("pause")
        if(opcion_perfumes == 2):
            main_categorias()
            os.system("pause")
        if(opcion_perfumes == 3):
            main_factura()
            os.system("pause")    
        else:
            print("esa opcion no existe")

main()