import csv


inventario = []
def menu():
    print("agregar producto en inventario")
    print("revisar inventario")
    print("clasificar inventario")
    print("salir")
   
def agregar_producto(inventario):
    id = input("ingrese el id")
    nombre = input("ingrese su nombre")
    categorias = input("")
    precio =int(input("ingrese el precio"))
    with open("inventario.csv", "a", newline='')as inventario:
        escritor_producto=csv.writer(inventario) 
        escritor_producto.writerow([id,nombre,categorias,precio])
    print ("el producot de id, nombre,categorias, precio es ")
    print(id)    
    print(nombre)
    print(categorias)
    print(precio)
    def ver_inventario():
        with open ("inventario.csv","r",newline="")as inventario:
            leer_archivo=csv.reader(inventario)
            for row in leer_archivo:
                id,nombre,categorias,precio=row
        print(f"id:{id}, nombre{nombre},categorias{categorias},precio{precio}")        
    def clasificar_productos():
        categorias = {
            "electronica":[],
            "textil":[],
            "calzado":[]
                   }
        with open("inventario.csv","r",newline="") as inventario:
            leer_archivo = csv.reader(inventario)
            for row in leer_archivo:
                id,nombre,categorias,precio = row
                producto=(id,nombre,categorias,precio)
                if categorias.lower()=="electronica":
                    categorias["electronica"].append(producto)
                elif categorias () =="textil":
                    categorias ["textil"].append (producto)
                elif categorias()=="calzado":
                     categorias ["calzado"].append(producto)
                else:
                     print (f"producto{nombre}en {categorias}")
        with open("clasificacion_productos.txt", "W") as clasificacion_deproductos:
            clasificacion_deproductos.write
            for producto in categorias["textil"]:
                clasificacion_deproductos.write(producto)
            clasificacion_deproductos.write
            for producto in categorias["calzado"]:
                clasificacion_deproductos.write(producto)
        print ("clasificacion")
        while True:
            opcion = menu()
            if opcion == "1":
                agregar_producto
            if opcion == "2":
                ver_inventario
            if opcion == "3":
                clasificar_productos    


             
                    
                    





    

   


    
        




