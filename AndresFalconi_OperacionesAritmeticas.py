def operacionesAritmeticas(num1,num2,):  #Creamos la operacion , y las variables de los parametros que vamos a utilizar
    suma = num1+num2  #Creamos una variable que sume las 2 variables
    print("La suma es: ", suma ) 
    resta = num1-num2   #Creamos una variable que reste las 2 variables
    print("La esta es: ", resta)
    multi = num1*num2   #Creamos una variable que multiplique las 2 variables
    print("la multiplicacion es: ", multi)
    division = num1/num2   #Creamos una variable que divida las 2 variables
    print("La division es: ", division)
    potencia = num1**num2  #Creamos una variable que a la primera variable la eleve a la segunda variable
    print("La potencia es:", potencia)
#ingresamos los parametros por consola
operacionesAritmeticas(int(input("Ingrese el primer numero: ")), int(input("Ingrese el segundo numero: ")))