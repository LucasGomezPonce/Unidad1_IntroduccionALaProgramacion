
contador = 0



while True:
    
    tiempo = int(input("Ingrese el tiempo del tramo: "))
    if tiempo == 0 :
        break    
    contador += tiempo 
    
horas = contador // 60

minutos = contador % 60

print(f"El tiempo total del viaje es:{horas}:{minutos}")

