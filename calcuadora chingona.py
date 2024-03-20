import random

def suma(a, b):
    return f"{a} + {b} = sonora ma puchaina"

def resta(a, b):
    return f"{a} - {b} = valiendo vrg joven "

def multiplicacion(a, b):
    return f"{a} * {b} =  me lleve 3 fokin horas haciendo esta mrd "

def division(a, b):
    return f"{a} / {b} = ya vales vrg si no jala. "

def respuesta_meme():
    memes = [
        "¿te pica la puchaina? ",
        "ven bieja hija de la gran pocta te voy a meter el bicho ",
        "hay dios mio estoy bellako ",
        "shupa me la polla ",
        "grita cantoe puerca",
        "no seas credulo mc fly"
        "no sere spiderman pero si te agarro la araña canto ijuela gran poctaa"
        ]
    return random.choice(memes)

def main():
    print("¡Bienvenido a la Calculadora chingona!")
    while True:
        try:
            a = float(input("Ingresa el primer maldito  número: "))
            operador = input("Ingresa el operador (+, -, *, /): ")
            b = float(input("Ingresa el segundo  ijueputa número: "))

            if operador == "+":
                resultado = suma(a, b)
            elif operador == "-":
                resultado = resta(a, b)
            elif operador == "*":
                resultado = multiplicacion(a, b)
            elif operador == "/":
                resultado = division(a, b)
            else:
                print("Operador no válido. no seas 0te maje ya la cagas ")
                continue
            print(respuesta_meme())
            print(f"Respuesta: {resultado}\n")
        except ValueError:
            print("Ingresa números válidos. es que para idiota no se estudia vea .")

if __name__ == "__main__":
    main()