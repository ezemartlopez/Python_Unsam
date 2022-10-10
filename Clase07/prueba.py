import csv
list =  ['nombre,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
lineas = csv.reader(list, delimiter=',')
for line in lineas:
    print(line)
