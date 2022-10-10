from datetime import timedelta
from datetime import date
from datetime import datetime

def vida_en_segundos(fecha_nac):
    """a la que le pasás tu fecha de nacimiento y te devuelve la cantidad de segundos que viviste (asumiendo que naciste a las 00:00hs 
    de tu fecha de nacimiento). La función debe tomar como entrada una cadena en formato 'dd/mm/AAAA' (día, mes, año con 2, 2 y 4 dígitos, 
    separados con barras normales) y devolver un float"""
    dia_nacimiento = datetime.strptime(fecha_nac, '%d/%m/%Y')
    hoy = datetime.now() + timedelta()
    tiempo = hoy - dia_nacimiento
    segundos_totales = tiempo.total_seconds()
    return segundos_totales

if __name__=='__main__':
    print(vida_en_segundos('14/12/1997'))
    print(datetime.now() + timedelta())