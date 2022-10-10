class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

class TorreDeControl:
    """Representa una torre de control, que opera con vuelos de llegada y partido al aeropuerto
    cuenta con las siguientes operaciones: 
    1) nuevo_arribo(cod_avion): dado un codigo de un vuelo de un avion lo coloca el la cola de arribos(FIFO), 
    2) nueva_partida(cod_avion): dado un codigo de un vuelo de un avion lo coloca en la cola de partidas(FIFO),
    3) ver_estado(): muestra el estado de la torre de control indicando si tiene vuelos esperando a aterrizar o despegar 
    4) asignar_pista: asigna una pista a un vuelo dando prioridad a los vuelos de arribo al aeropuerto (FIFO) y despues a los de partida de aeropuerto
    """
    def __init__(self):
        self.arribos = Cola()
        self.partidas = Cola()
    def nuevo_arribo(self,cod_avion):
        self.arribos.encolar(cod_avion)
    
    def nueva_partida(self,cod_avion):
        self.partidas.encolar(cod_avion)

    def ver_estado(self):
        aterrizar = f"Vuelos esperando para aterrizar: {', '.join(self.arribos.items)}" 
        despegar = f"Vuelos esperando para despegar: {', '.join(self.partidas.items)}" 
        return aterrizar + "\n" + despegar
        #print('Vuelos esperando para aterrizar: '+ aterrizar)
        #print('Vuelos esperando para despegar: '+ despegar)
    
    def asignar_pista(self):
        vuelo = ''
        tipo  = ''
        if not self.arribos.esta_vacia():
            vuelo = self.arribos.desencolar()
            tipo = 'arribo'
        elif not self.partidas.esta_vacia():
            vuelo = self.partidas.desencolar()
            tipo = 'despego'
        else:
            return "No hay vuelos en espera."
        return f"El vuelo {vuelo} {tipo} con exito"


if __name__=='__main__':
    torre = TorreDeControl()
    torre.nuevo_arribo('AR156')
    torre.nueva_partida('KLM1267')
    torre.nuevo_arribo('AR32')
    
    print(torre.ver_estado())
    
    print(torre.asignar_pista())
    
    print(torre.asignar_pista()) 
    
    print(torre.asignar_pista())
    
    print(torre.asignar_pista())
    
