ps= "shazam"
cn= input("ingrese la contraseña: ")
if cn == ps .upper():
    print ("Clave correcta")    
else:
    print ("Contraseña incorrecta ")

print ("--------------------------------------------------------")


nom = input("ingrese su nombre de usuario: ")
if len(nom)>4:
    print("debe ser como minimo 4 carcteres")
elif len (nom)<10:
    print ("Error el limte es de 10 caracteres")
else:
    print("Usuario creado de manera correcta")

print ("--------------------------------------------------------------------------------------------------------------------")


pn= int(input("Ingrese el pin: "))
if len (str(pn))==4:
    print("codigo correcto")
else:
    print("codigo erroneo")

 