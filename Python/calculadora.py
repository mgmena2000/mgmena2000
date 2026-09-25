salir = False
acumulado = 0

def suma(auxacumulado, auxsumando):    
    return float(auxacumulado) + float(auxsumando) 

def resta(auxacumulado, auxsumando):    
    return float(auxacumulado) - float(auxsumando) 

def multiplicacion(auxacumulado, auxsumando):    
    return float(auxacumulado) * float(auxsumando) 

def division(auxacumulado, auxsumando):    
    return float(auxacumulado) / float(auxsumando)

def cuadrado():
    x = int(input('x: '))
    y = int(input('y: '))
    strx = ' '
    for b in range (0, y):
        strx = strx + '_ '
    print(strx)    
    for a in range (0, x):
        strx = '|'
        for b in range (0, y):
            strx = strx + '_|'
        print(strx)
        
while not salir:
    print('Acumulado: ', acumulado)
    print()
    print('1.- Suma');
    print('2.- Resta');
    print('3.- Multiplicación');
    print('4.- División');
    print('5.- Cuadrado');
    print('0.- Salir');
    opcion = int(input('Opción: '))    
    match opcion: 
        case 1:            
            acumulado = suma(acumulado, input(str(acumulado) + ' + '))
        case 2:            
            acumulado = resta(acumulado, input(str(acumulado) + ' - '))
        case 3:            
            acumulado = multiplicacion(acumulado, input(str(acumulado) + ' *'))
        case 4:            
            acumulado = division(acumulado, input(str(acumulado) + ' / '))
        case 5:
            cuadrado()
        case 0:
            salir = True
    print()       

print('Adios')
