# canguro_buenos.py

class Canguro:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre, contenido=None):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        if contenido == None:
            contenido = []
        self.contenido_marsupio = contenido
    
    def __repr__(self) -> str:
        return self.nombre
    
    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        if self.contenido_marsupio:
            for obj in self.contenido_marsupio:
                s = '    ' + object.__str__(obj)
                t.append(s)
        else:
            t.append('    '+'Nada')
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#Para no interferir con el codigo voy a comentar a continuacion
#class Canguro:
#    """Un Canguro es un marsupial."""
#    # Gracias a los comentarios que pude observar en el grupo de Slack
#    # el problema radica en los valores que se pasan por defecto a la funcion __init__ de la clase canguro
#    # ya que deben ser valores inmutables, en nuestro caso produjo que el cangurito al meterse en la bolsa 
#    # de madre_canguro copiara todo su contenido a su bolsa.
#    def __init__(self, nombre, contenido=[]):
#        """Inicializar los contenidos del marsupio.
#
#        nombre: string
#        contenido: contenido inicial del marsupio, lista.
#        """
#        self.nombre = nombre
#        self.contenido_marsupio = contenido # Aqui esta el problema
#================================================================

if __name__=='__main__':
    madre_canguro = Canguro('Madre')
    cangurito = Canguro('gurito')
    madre_canguro.meter_en_marsupio('billetera')
    madre_canguro.meter_en_marsupio('llaves del auto')
    madre_canguro.meter_en_marsupio(cangurito)
    #for el in madre_canguro.contenido_marsupio:
    #    print(el)
    print(madre_canguro)
    #print("#############")
    print(cangurito)