import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['recetario']
# Crear una base de datos llamada "recetario" si no existe, en caso contrario utilizarla
categoria = mydb["categoria"]  # <class 'pymongo.collection.Collection'>
receta = mydb["receta"]
ingredientes = mydb["ingredientes"]

def agregar_receta():
    """Agrega una nueva categoria a la BD"""
    nombre =input('Introduzca el nombre de la receta: ')
    instrucciones =input('Introduzca el las intrucciones de la receta: ')
    categoria = int(input('Indique a que categoría pertenece la receta (1-Entrantes, 2-Platos Principales, 3-Postres, 4-Otros)'))
    id = receta.count_documents + 1 if receta.count_documents else 0
    insertar = {'nombre':  nombre,'instrucciones': instrucciones, '_id': id}
    receta.insert_one(insertar)
    print("La receta se ha guardado correctamente") 
    
def eliminar_receta():
    """Elimina una receta por su ID"""
    id=int(input('Ingrese el número de la receta que desea borrar: ')) 
    receta.delete_one({'_id' : id})
    print("Se ha eliminado la receta con éxito.")   

def buscar_receta(): 
    """Busca una receta por su nombre y devuelve todos los campos"""  
    nombre = input ('¿Qué receta deseas buscar? ')
    resultado = receta.find_one ({ 'nombre' : nombre })
    if not resultado:
        print ("No hay ninguna receta registrada bajo ese nombre.")
    else:
        print(f'\nNombre: {resultado ["nombre"]}\nInstrucciones:{resultado ["instrucciones"]}\nID: {resultado ["_id"]}')

def actualizar_receta(): 
    """Actualiza un campo específico de una receta"""
    _id = int (input ('Indica el número de la receta que quieres editar: '))
    Campo = input ('Que campo deseas modificar?').lower()
    valor = input ('¿Cuál es el nuevo valor para este campo?')
    if Campo == 'nombre':
        receta.update_one({'_id':_id},{'$set':{Campo:valor}})
    elif Campo=='instrucciones':
        receta.update_one({'_id':_id},{'$set':{"instrucciones."+Campo:valor}})
        
    else:
        print ("El campo introducido no es válido.")
        return
    print ("Los datos han sido actualizados correctamente.")

def ver_recetas():
    """Devuelve todas las recetas en formato tabla"""
    print("%-20s %-50s %-70s"%("ID","Nombre", "Instrucciones"))
    for i in receta.find():
        print("%-20d %-50s %-70s"%(i['_id'],i['nombre'], i['instrucciones']))


def main():
   
    while True:
        print("\n--- Menú ---")
        print("a) Agregar nueva receta")
        print("c) Actualizar receta existente")
        print("d) Eliminar receta existente")
        print("e) Ver listado de recetas")
        print("f) Buscar ingredientes y pasos de receta")
        print("g) Salir")

        opcion = input("Seleccione una opción: ").lower()

        if opcion == 'a':
            agregar_receta()
        elif opcion == 'c':
            actualizar_receta()
        elif opcion == 'd':
            eliminar_receta()
        elif opcion == 'e':
            ver_recetas()
        elif opcion == 'f':
            buscar_receta()
        elif opcion == 'g':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()