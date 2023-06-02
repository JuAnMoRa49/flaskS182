
def menu (eleccion):
    
    print ("Menu de operaciones a realizar")
    print ("1.- Dar de alta un producto")
    print ("2.- Dar de baja un producto")
    print ("3.- Actualizar un producto")
    print ("4.- Mostrar productos")
    print ("5.- Promedio de productos")
    print ("6.- Total bebidas de una marca")
    print ("7.- Consultar por clasificacion")
    eleccion=int(input("Ingresa que quieres realizar"))
    
    
    if (eleccion==1):
        
        nom=str(input("Ingresa el nombre del producto"))
        pre=float(input("Ingresa el precio del producto"))
        print ("Menu de clasificacion")
        print ("1.- Agua, 2.- Bebida aazucarada, 3.-Bebida energética, 4.-Otro")
        cla=int(input("Ingresa la clasificacion por numero"))
        mar=str(input("Ingresa la marca del producto"))
        daralta(nom, pre, cla, mar)
        
    
    elif (eleccion==2):
        
        idbaja=int(input("Ingresa el id del producto que deseas eliminar"))
        darbaja(idbaja)
        
        
    elif (eleccion==3):
        
        idactualizar=int(input("Ingresa el id del producto que quieres actualizar"))
        newnom=str(input("Ingresa el nombre nuevo del producto"))
        newpre=str(input("Ingresa el nuevo precio del producto"))
        print ("1.- Agua, 2.- Bebida aazucarada, 3.-Bebida energética, 4.-Otro")
        newcla=int(input("Ingresa la nueva clasificacion por numero"))
        newmar=str(input("Ingresa la nueva marca del producto"))
        actualizar(newnom, newpre, newcla, newmar)
    
    
    elif(eleccion==4):
        
        mostrar()
        
    
    elif(eleccion==5):
        
        sum= sum
        promedioproductos()
        
    
        
        
        
        
        
        
        
def daralta (id, nombre, precio, clasificacion, marca):
    
    return("Se realizo la alta del producto")


def darbaja (id):
    
    return("Se realizo la baja del producto")


def actualizar (id, nombre, precio, clasificacion, marca):
    
    return ("Se realizo la actualizacion del producto")

def mostrar ():
    
    return ("Productos")

def promedioproductos (precio):
    
    return ("El promedio de los precios de los productos es:")

def bebidamarca (marca):
    
    return ("Los productos de la marca ", marca, " son ")

def clasificacion (clasificacion):
    
    return ("Los productos de tipo ", clasificacion, " son ")