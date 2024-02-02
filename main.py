from Persona import Persona
from menu import *

def main():
    censo = Persona.generar_censo(50000)
    print(censo[-1])
    principal_menu(censo)


if __name__ == "__main__":
    main()
