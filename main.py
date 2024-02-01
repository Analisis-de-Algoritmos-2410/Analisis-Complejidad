from Persona import generar_censo
from plotter import generar_reporte

def main():
    censo = generar_censo(50000)
    print(censo[-1])
    generar_reporte()


if __name__ == "__main__":
    main()
