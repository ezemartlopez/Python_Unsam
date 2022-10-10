class Lote:
    def __init__(self, nombre, cajones, precio):
        # Todo dato guardado en `self` es propio de esa instancia
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    def __str__(self) -> str:
        return f"Lote de {self.cajones} de {self.nombre}, pagados a ${self.precio} cada uno."
    def __repr__(self):
        return f"Lote({self.nombre},{self.cajones},{self.precio})"
    
    def costo(self):
        return self.cajones * self.precio

    def vender(self,cajones_vendidos):
        #si el numero de cajones vendidos supera al stock, por mi criterio lo igualo a cero
        if cajones_vendidos > self.cajones:
            self.cajones = 0
        else:
            self.cajones -= cajones_vendidos
    def listar_variables(self):
        lista = [self.nombre,self.cajones,self.precio]
        return lista
if __name__=='__main__':
    obj = Lote('Pera',120,23.9)
    print(obj)