import jitari_llamada

jitari = []

while True:
    print("\n-----Lista de objetos para la cuaresma-----\n")
    print("1. Agregar un objeto")
    print("2. Ver los objetos")
    print("3. Eliminar objetos")
    print("4. Buscar objetos")
    print("5. Salir del programa")
    
    pregunta = input("\nBuenos dias, ¿que desea hacer?: ")
    
    if pregunta == "1":
        jitari_llamada.agregar_objeto(jitari)
        
    elif pregunta == "2":
        jitari_llamada.ver_objetos(jitari)
        
    elif pregunta == "3":
        jitari_llamada.eliminar_objeto(jitari)
        
    elif pregunta == "4":
        jitari_llamada.buscar_objeto(jitari)
        
    elif pregunta == "5":
        print("Saliendo... ¡Hasta luego!")
        break
        
    else:
        print("Opción no válida. Por favor, escriba un número del 1 al 5.")