import random
import math

def generar_coordenadas(n):
    matriz = []
    for _ in range(n):
        x = random.randint(-81, 81)
        y = random.randint(-81, 81)
        matriz.append([x, y])
    return matriz


def distancia_origen(coordenada):
    x, y = coordenada
    return math.sqrt(x**2 + y**2)


def mas_alejada(coordenadas):
    if not coordenadas:
        return None 
    if len(coordenadas) == 1:
        x, y = coordenadas[0]
        if x > 0 and y < 0:
            return coordenadas[0]
        else:
            return None
    mid = len(coordenadas) // 2
    izq = mas_alejada(coordenadas[:mid])
    der = mas_alejada(coordenadas[mid:])

    if izq and der:
        return izq if distancia_origen(izq) > distancia_origen(der) else der
    elif izq:
        return izq
    else:
        return der


def main():
    n = int(input("Ingrese la cantidad de pares de coordenadas: "))
    matriz = generar_coordenadas(n)
    
    print("Coordenadas generadas:")
    for par in matriz:
        print(par)

    resultado = mas_alejada(matriz)

    if resultado:
        print(f"\nLa coordenada mas alejada con X>0 e Y<0 es: {resultado}")
        print(f"Distancia al origen: {distancia_origen(resultado):.2f}")
    else:
        print("\nNo hay coordenadas con X>0 e Y<0.")

main()