"""
ingregiente
modelo sencillo para un ingrediente.
atributos:
   - Nombre - nombre del ingrediente.
   - Cantidad - cantidad necesaria del ingrediente.
   - Unidad - unidad de medida para el ingrediente. 
"""


class Ingrediente:
    def __init__(self, nombre='', cantidad=None, unidad=''):
        self._nombre = nombre
        self._cantidad = cantidad
        self._unidad = unidad
    
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
    
    # CANTIDAD
    @property
    def cantidad(self):
        return self._cantidad
    @cantidad.setter
    def cantidad(self, valor):
        self._cantidad = valor
    @cantidad.deleter
    def cantidad(self):
        del self._cantidad
    
    # UNIDAD
    @property
    def unidad(self):
        return self._unidad
    @unidad.setter
    def unidad(self, valor):
        self._unidad = valor
    @unidad.deleter
    def unidad(self):
        del self._unidad
    
    def __str__(self):
        return f""" Nombre: {self.nombre}
 cantidad: {self.cantidad} {self.unidad}"""
    
    
    