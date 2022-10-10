# camion.py
"""
@Autor: Martinez Lopez Ezequiel
"""
"""El __str__ pretende ser lo más legible para el ser humano, 
mientras que el __repr__ debe ser algo que pueda usarse para recrear el objeto, 
aunque a menudo no será exactamente como se creó, como en este caso."""

class Camion:

    def __init__(self, lotes):
        #crea el atributo lotes y le asigna lo que recibe por parametro, es decir una lista de lotes
        self.lotes = lotes

    def __iter__(self):
        #devuelve un iterable del atributo lotes
        return self.lotes.__iter__()
    
    def __contains__(self, nombre):
        #verifica si tiene contenido en su atributo lotes el nombre requerido
        return any(lote.nombre == nombre for lote in self.lotes)
    
    def __len__(self):
        #devuelve la longitud del atributo lotes (lista)
        return len(self.lotes)
    
    def __getitem__(self,indice):
        #devuelve la porcion de lista segun el rango de indices
        return self.lotes[indice]
    
    def __repr__(self):
        """devuelve la representación de cadena "oficial" de un objeto. Si es 
        posible, esto debería parecerse a una expresión de Python válida que 
        podría usarse para recrear un objeto con el mismo valor (dado un entorno apropiado)."""

        s = 'Camion(['
        lotes = (lote.__repr__() for lote in self.lotes)
        s += ','.join(lotes)+'])'
        return s
    def __str__(self):
        """devuelve la representación de cadena "informal" de un objeto"""
        s = f'Camion con {len(self)} lotes:\n'
        for lote in self.lotes:
            s += f'Lote de {lote.cajones} cajones de {lote.nombre}, pagados a ${lote.precio} cada uno.\n'
        return s

    def precio_total(self):
        #devuelve la suma de los costos de cada lote a traves de una expresion generadora
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total

if __name__=='__main__':
    # Para que funcionen las pruebas correctamente deberia colocarse en la misma carpeta que la clase 10
    #con las versiones de lote.py e informe_final.py mas recientes, ya que son las que necesita para sus pruebas
    import informe_final
    camion = informe_final.leer_camion('../Data/camion.csv')#solo necesita la funcion leer_camion()
    print("-------- Prueba de metodo especial __str__ ---------")
    print(camion)

    print("-------- Prueba de metodo especial __repr__ ---------")
    print(repr(camion))
    print("\n")
    print("-------- Prueba de metodo especial __len__ ---------")
    print(f"La longitud del camion es: {len(camion)}")
    print("\n")
    print("-------- Prueba de metodo especial __getitem__ ---------")
    print(camion[0:4])
    print("\n")
    print("-------- Prueba de metodo especial __contains__ ---------")
    print('Naranja' in camion)
    print('Manzana' in camion)
    print("\n")
    print("-------- Prueba de metodo especial __iter__ ---------")
    for lote in camion:
        print(lote)
    print("\n")
    print("-------- Prueba de metodo precio_total() ---------")
    print(camion.precio_total())
    print("\n")
    print("-------- Prueba de metodo contar_cajones() ---------")
    print(camion.contar_cajones())