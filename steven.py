#nombre= input("ingrese su nombre: ")
#print(f"hola {nombre}")
#----------------------------------------------------------------------------------------

#num= int(input("coloque un numero: "))
#an= num-1 
#my= num+1 
#print(f"el antesesr de {num} es : {an} \ny el sucesor de {num} es : {my} ") 

#-------------------------------------------------------------------------------------------
#Un colegio tiene 3 salas. Se quiere reemplazar los escritorios de esas salas, cada desk cabe 2 alumnos
#Escribe un programa que recibe a, b y c como los numeros de alumnos en cada sala, quiero que entregues 

#"Necesito 10 escritorios para sala A" a = 20
#"Necesito 15 escritorios para sala B" b = 29
#"Necesito 13 escritorios para sala C" c = 25
#"Se Necesita comprar 38 Escritorios en total"
a= int(input("ingrese la cantidade  alumnos para la sala a: "))
print(a)
b=int(input("ingrese la cantidade  alumnos para la sala b: "))
print(b)
c=int(input("ingrese la cantidade  alumnos para la sala c: "))
print(c)
if a % 2 == 0:  #si a es par se /2  
    sa= a // 2

else:
    sa= a // 2 +1
#----------------------
if b % 2 == 0:  #si a es par se /2  
    sb= b // 2

else: 
    sb= b // 2 +1  #si a es par se /2  
#------------------------
if   c % 2 == 0:  
    sc= c // 2 

else: 
    sc= c // 2 +1
total= sa+sb+sc 
print (f"Necesito esta cantidad de escritorios {sa} para la sala a ")
print (f"Necesito esta cantidad de escritorios {sb} para la sala b ")
print (f"Necesito esta cantidad de escritorios {sc} para la sala c ")
print (f"El total de escritorios es: {total}")







