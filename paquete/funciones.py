from paquete.clases import Persona, Cliente, Empleado
import re

def no_numeric(ingreso):
    if re.fullmatch(r"[a-zA-Z]+", ingreso): # fullmatch verifica la expresion para todos los carácteres
        return True
    else:
        print("El campo ingresado no puede estar vacio ni contener carácteres numéricos\n\r")
        return False

def only_numeric(ingreso):
    if re.fullmatch(r"\d+", ingreso):
        return True
    else:
        print("El campo ingresado no puede estar vacio y solo puede contener carácteres numéricos\n\r")
        return False

def ingresa_datos_cliente():
    ingreso = str(input("\n\rIngresa el nombre del cliente: "))
    while no_numeric(ingreso)==False:
        ingreso = str(input("Ingresa el nombre del cliente: "))
    nombre = ingreso

    ingreso = str(input("\n\rIngresa el apellido del cliente: "))
    while no_numeric(ingreso)==False:
        ingreso = str(input("Ingresa el apellido del cliente: "))
    apellido = ingreso

    ingreso = (input("\n\rIngresa el teléfono del cliente: "))
    while only_numeric(ingreso)==False:
        ingreso = str(input("Ingresa el teléfono del cliente: "))
    telefono = ingreso

    ingreso = (input("\n\rIngresa el dni del cliente: "))
    while only_numeric(ingreso)==False:
        ingreso = str(input("Ingresa el dni del cliente: "))
    dni = ingreso
    return Cliente(nombre, apellido, telefono, dni)
