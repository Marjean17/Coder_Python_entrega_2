from IPython.display import clear_output
from paquete.clases import Persona, Cliente, Empleado
from paquete.funciones import no_numeric, only_numeric, ingresa_datos_cliente


salir=False
lista_clientes = []
cliente_1 = Cliente("Mariano", "Jeanneret", 1234, 2847)
cliente_2 = Cliente("Martin", "Jeanneret", 5678, 9999)
cliente_2.set_estado(False)
lista_clientes.append(cliente_1)
lista_clientes.append(cliente_2)
print(lista_clientes[0])
print(lista_clientes[1])
while salir==False:
  try:
    opcion = int(input("""\n\rIngresa el nro correspondiente a la opción elegida
----------------------------------------------
1.- Registrar cliente
2.- Mostrar clientes
3.- Modificar cliente
4.- Borrar cliente

0.- Salir

opción seleccionada: """))
  except ValueError:
    clear_output()
    print("La opción seleccionada no es válida, intenta nuevamente\n\r")


  if opcion == 1: # Registrar cliente

    cliente_registrado = lista_clientes.append(ingresa_datos_cliente())
    indice = len(lista_clientes)-1
    print(f"\n\rSe ha ingresado correctamente al siguiente cliente{lista_clientes[indice]}")

  if opcion == 2: # Mostrar clientes
    if len(lista_clientes) > 0:
      print("Clientes registrados:")
      for cliente in lista_clientes:
        if cliente.get_estado() == True: # solo mostramos activos
           print(cliente)
    else: print("no hay clientes registrados")

  if opcion == 3:  #  Modificar cliente
    cliente_buscado = input("\n\rIngrese el Apellido o nro de Dni del cliente a modificar: ")
    for cliente in lista_clientes: 
        if cliente_buscado == cliente.get_apellido() or cliente_buscado == str(cliente.get_dni()):  # Compara apellido y DNI
            indice = lista_clientes.index(cliente)
            print(f"\n\rCliente encontrado:{cliente_buscado}\n\rRatifique o rectifique los datos del mismo")
            lista_clientes[indice] = ingresa_datos_cliente()
            print(f"\n\rSe ha ingresado correctamente al siguiente cliente{lista_clientes[indice]}")
            break  # Sale del bucle si se encuentra el cliente
    else: print("no existe un cliente registrado con el dato proporcionado")

  if opcion == 4:  # Baja cliente (mediante baja lógica)
    cliente_buscado = input("\n\rIngrese el Apellido o nro de Dni del cliente a borrar: ")
    for cliente in lista_clientes:
        if cliente_buscado == cliente.get_apellido() or cliente_buscado == str(cliente.get_dni()):  # Compara apellido y DNI
            baja = input(f"\n\rCliente encontrado:{cliente_buscado}\n\rSeguro que desea eliminar?\n\rIngrese SI para eliminar o NO para cancelar \n\r\n\rOpción elegida: ").upper()
            if baja == "SI":
                lista_clientes.remove(cliente)
                print("\n\rSe ha eliminado correctamente al cliente seleccionado")
                  # Sale del bucle si se encuentra el cliente
            else: 
                print("Cliente no borrado")
            break
    else: print("no existe un cliente registrado con el dato proporcionado")


  if opcion == 0:
    salir = True
