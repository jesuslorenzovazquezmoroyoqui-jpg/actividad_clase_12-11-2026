def agregar_objeto(lista):
    cosa = input("Agregue las cosas de la cuaresma. Si ya no quiere agregar mas, presione (1): ")
    if cosa == "1":
        return
    lista.append(cosa)
    print(f"Objeto '{cosa}' añadido a la lista.")

def ver_objetos(lista):
    print("\n--- Lista de objetos añadidos ---")
    if len(lista) > 0:
        for i in lista:
            print(f"- {i}")
    else:
        print("No hay objetos en la lista.")

def eliminar_objeto(lista):
    if len(lista) > 0:
        print("\n--- Objetos actuales ---")
        for i in lista:
            print(f"- {i}")
        
        objeto_eliminar = input("Seleccione el objeto que quiera eliminar: ")
        
        if objeto_eliminar in lista:
            lista.remove(objeto_eliminar)
            print("Objeto", objeto_eliminar, "ha sido eliminado.")
        else:
            print("Objeto no encontrado.")
    else:
        print("No hay objetos en la lista para eliminar.")

def buscar_objeto(lista):
    if len(lista) > 0:
        while True:
            obj_buscar = input("\nEscriba el nombre del objeto que quiera buscar, si no, escriba (salir): ")
            
            if obj_buscar.lower() == "salir":
                break
                
            encontrado = False
            for item in lista:
                if item.lower() == obj_buscar.lower():
                    print(f"✅ El objeto '{item}' sí está en la lista.")
                    encontrado = True
                    break
            
            if encontrado:
                break
            else:
                print("Objeto no encontrado, vuelva a intentar otra vez.")
    else:
        print("No hay objetos en la lista para buscar.")