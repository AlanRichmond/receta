"""
receta
Modelo sencillo de receta de cocina
Atributos:
   - ingredientes -- lista de ingredientes 
   - pasos        -- lista de instrucciones
   - nombre       -- nombre de la receta
comportamientos:
   - menu         -- menu de operaciones
   - agregar ingregientes -- permite agregar ingredientes
   - consultar ingredientes -- consultar ingredientes en la receta
   - agregar pasos       -- permite agregar instrucciones
   - sonsultar pasos     -- permite consultar las instrucciones
"""

from clase_ingrediente import Ingrediente
import os

class Receta:
    OPC_AGREGAR_INGREDIENTES = 1
    OPC_CONSULTAR_INGREDIENTES = 2
    OPC_AGREGAR_PASO = 3
    OPC_CONSULTAR_PASOS = 4
    OPC_SALIR = 0

    def __init__(self, nombre=''):
        self._nombre = nombre
        self._ingredientes = []
        self._pasos = []
    
    def __str__(self):
        s = f'          {self.nombre} '
        s += "\nIngredientes:\n "
        for ingredientes in self.ingredientes:
            s += f"{ingredientes}\n"
        s += "\nPasos: \n"
        for i, paso in enumerate(self.pasos):
            s += f"{i+1}. {paso}\n"
        return s
    
    # NOMBRE
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    @nombre.deleter
    def nombre(self):
        del self._nombre
    
    # INGREDIENTES
    @property
    def ingredientes(self):
        return self._ingredientes
    @ingredientes.setter
    def ingredientes(self, valor):
        self._ingredientes = valor
    @ingredientes.deleter
    def ingredientes(self):
        del self._ingredientes
    
    # PASOS
    @property
    def pasos(self):
        return self._pasos
    @pasos.setter
    def pasos(self, valor):
        self._pasos = valor
    @pasos.deleter
    def pasos(self):
        del self._pasos
    
    def menu(self):
        continuar = True
        while continuar:
            os.system("cls")
            print("----- BIENVENIDO -----\n")

            print(f"""     {self.nombre}
{self.OPC_AGREGAR_INGREDIENTES}) Agregar ingredientes
{self.OPC_CONSULTAR_INGREDIENTES}) Consultar ingredientes
{self.OPC_AGREGAR_PASO}) Agegar pasos
{self.OPC_CONSULTAR_PASOS}) Consultar pasos
{self.OPC_SALIR}) Salir """)
            opc = input("Seleccione una opcion..")
            try:
                opc = int(opc)
            except:
                opc = -1
            if opc == self.OPC_AGREGAR_INGREDIENTES:
                self.agregar_ingredientes()
            
            elif opc == self.OPC_CONSULTAR_INGREDIENTES:
                self.consultar_ingredientes()
            
            elif opc == self.OPC_AGREGAR_PASO:
                self.agregar_paso()
            
            elif opc == self.OPC_CONSULTAR_PASOS:
                self.consultar_pasos()
            
            elif opc == self.OPC_SALIR:
                continuar = False
            
            else:
                print("Opcion no valida.")
            input("Precione enter para continuar..")
        print("Nos vemos.")

    
    def agregar_ingredientes(self):
        continuar = True
        while continuar:
            os.system("cls")
            print("          Agregar Ingredientes")
            nombre = input("Nombre: ")
            cantidad = -1
            while cantidad <= 0:
                cantidad = input("Cantidad: ")
                try:
                    cantidad = float(cantidad)
                except:
                    cantidad = 0
            unidad = input("Unidad de medida: ")
            ingrediente = Ingrediente(nombre, cantidad, unidad)
            self.ingredientes.append(ingrediente)
            respuesta = input("Desea agregar otro ingresiente (s/n) ")
            if respuesta != "s" and respuesta != "S":
                continuar = False



    def consultar_ingredientes(self):
        os.system("cls")
        print("                   Ingredientes")
        if len(self.ingredientes) == 0:
            print("No hay ingredientes registrados")
        else:
            for ingrediente in self.ingredientes:
                print(f"{ingrediente}")
                print("*"*40)


    def agregar_paso(self):
        continuar = True
        while continuar:

            os.system("cls")
            print("               Agregar paso")
            paso = input("Paso: ")
            self.pasos.append(paso)
            respuesta = input(" Desea agregar otro paso (s/n) ")
            if respuesta != "s" and respuesta !="S":
                continuar = False
            


    def consultar_pasos(self):
        os.system("cls")
        print("                  Pasos")
        if len(self.pasos) == 0:
            print(" No hay pasos registrados.")
        else:
            for i, paso in enumerate(self.pasos):  # DEVUELVE LOS VALORES DESDE 0  
                print(f"{i+1}. {paso}")
                print("*"*40)





