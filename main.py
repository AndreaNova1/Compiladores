import re

def if_integer(string):
    reg_exp = "[-+]?\d+$"
    return re.match(reg_exp, string) is not None

def menu():
    val = True
    while val is True:
        try:
            print("Inicio")
            print("1. Operacion Adicion")
            print("2. Operacion Sustraccion")
            print("3. Operacion Producto")
            print("Si desea salir presione cualquier numero")
            opcion = int(input("\nSeleccione una opción del 1 al 3: "))
            if opcion ==1:
                escape = "p"
                r = "0"

                print("\nSe esta ejecutando la operacion de Adicion")
                while escape == "p":
                    try:
                        print("Para cancelar presione (c)")
                        adicion = input("\nIngrese un numero: ")

                        int(adicion)
                        r = float(r) + float(adicion)
                        print("El Resultado de la adicion es: ", float(r))
                    except ValueError:
                        if adicion== "p":
                            escape = "o"
                        else:
                            print("Lo siento no se puede realizar la adicion")
                            print("El resultado Total es: ", float(r))

            elif opcion ==2:
                escape = "p"
                r = "0"

                print("\nSe esta ejecutando la operacion de oooo")
                while escape == "p":
                    try:
                        print("Para cancelar presione (c)")
                        sustraccion = input("\nIngrese un numero: ")

                        int(sustraccion)

                        if r == "0":
                            r = sustraccion
                        else:
                            r = float(sustraccion) - float(r)
                    except ValueError:
                        if sustraccion == "p":
                            escape = "n"
                        else:
                            print("Lo siento no se puede realizar la adicion")
                            print("El resultado Total es: ", float(r))

            elif opcion == 3:
                escape = "p"
                r = "0"

                print("\nSe esta ejecutando la operacion del producto")

                while escape == "p":

                    try:
                        print("Si desea dejar de realizar la sustraccion presiones la tecla  (c)")
                        Producto = input("\nIngrese un numero: ")

                        int(Producto)

                        if r == "0":
                            r = Producto
                        else:
                            r = float(r) * float(Producto)
                        print("El total actual de la Multiplicación es: ", float(r))
                    except ValueError:
                        if Producto == "s":
                            escape = "n"
                        else:
                            print("Lo siento no se puede realizar el producto indicado")
            else:
                print("Cerrando programa")
                val= False

        except ValueError:
            print("\nNo se puede continuar, se encontro un error.")
            print("\n")
menu()
