print("Bienvenido al calculador para variable aleatoria discreta")
listax=[]
contador1=1
can1=int(input('ingrese la cantidad de variables : '))
while contador1 <= can1:
        var=int(input('Ingrese el {}° valor de x : '.format(contador1)))
        listax.append(var)
        contador1=contador1+1


listay=[]
contador2=1
while contador2 <= can1:
        prob=float(input('Ingrese las la probabilidad para el {}° valor de x : '.format(contador2)))
        listay.append(prob)
        contador2=contador2+1
               
print('\n')
print("           x : ",listax)
print("probabilidad : ",listay)
print('\n')

def sumaListas(a, b):
        s = []
        for i in range(len(a)):
                s.append(a[i] * b[i])
        return s
varXprob=sumaListas(listax,listay)

def sumar(lista):
        if len(lista)==1:
                return lista[0]
        else:
                return lista[0] + sumar(lista[1:])
espe=sumar(varXprob)

print("La esperanza matemática es : {}".format(espe))

def variancia(listax):
        sumatoria = 0
        sumatoria_2 = 0
        for i in range(len(listax)):
                sumatoria = sumatoria + ((listax[i]**2)*listay[i])
                var_final = sumatoria - (espe**2)
                        
        return var_final
varian = variancia(listax)

print("La variancia es: ", varian)
print("La desviación estandar es: ", (varian**(1/2)))
print("El coeficiente de variabilidad es : " , (varian**(1/2))/espe)
                
        
