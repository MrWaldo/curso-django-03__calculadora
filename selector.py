from resta import resta
from suma import suma
from division import division
from multiplicacion import multiplicacion

def selector(nro1: float, nro2: float, operador) -> None:
    if operador == "+":
        suma(nro1, nro2)
    elif operador == "-":
        resta(nro1, nro2)
    elif operador == "*" :
        multiplicacion(nro1, nro2)
    elif operador == "/" :
        division(nro1, nro2)
    else:
        print ("El operador ingresado es invalido, solo son admisibles los siguientes caracteres: /, *, -, +. \n intente correr el programa nuevamente")