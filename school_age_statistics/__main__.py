from datetime import datetime

from school_age_statistics.security.password import validar_contrasena
from school_age_statistics.data_entry.age_input import request_age_sample
from school_age_statistics.calculations.age_statistics import calcular_estadisticas
from school_age_statistics.ui.report import mostrar_reporte


def mostrar_fecha_inicio():
    """
    Muestra la fecha y hora cuando inicia la aplicación.
    """
    fecha_actual = datetime.now()

    print("=" * 55)
    print("Sistema de Estadísticas de Edades")
    print("Colegio San Pascualin")
    print("=" * 55)
    print(f"Fecha y hora de inicio: {fecha_actual.strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 55)


def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """
    print("\nMENÚ PRINCIPAL")
    print("1. Ingresar muestra de edades")
    print("2. Calcular estadísticas")
    print("3. Mostrar reporte")
    print("4. Salir")


def leer_opcion():
    """
    Solicita una opción del menú y valida que sea correcta.
    """
    while True:
        opcion = input("Seleccione una opción: ").strip()

        if opcion in ["1", "2", "3", "4"]:
            return opcion

        print("Opción inválida. Debe seleccionar una opción del 1 al 4.")


def ingresar_muestra_edades():
    """
    Llama la función encargada de solicitar la muestra de edades.
    """
    print("\nIngreso de muestra de edades")

    muestra_edades = request_age_sample()

    print("\nMuestra registrada correctamente.")
    print("Las edades ingresadas fueron:")
    print(muestra_edades)

    return muestra_edades


def opcion_calcular_estadisticas(muestra_edades):
    """
    Calcula las estadísticas de la muestra de edades ingresada.
    """
    if muestra_edades is None:
        print("\nPrimero debe ingresar una muestra de edades.")
        return None

    estadisticas = calcular_estadisticas(muestra_edades)

    print("\nEstadísticas calculadas correctamente.")
    print("Ya puede seleccionar la opción 3 para mostrar el reporte.")

    return estadisticas


def opcion_mostrar_reporte(muestra_edades, estadisticas):
    """
    Llama la función encargada de mostrar el reporte.
    """
    if muestra_edades is None:
        print("\nPrimero debe ingresar una muestra de edades.")
        return

    if estadisticas is None:
        print("\nPrimero debe calcular las estadísticas.")
        return

    reporte_mostrado = mostrar_reporte(muestra_edades, estadisticas)

    if reporte_mostrado:
        print("\nReporte mostrado correctamente.")
    else:
        print("\nNo se pudo mostrar el reporte porque faltan datos.")


def iniciar_aplicacion():
    """
    Función principal que controla el flujo del programa.
    """
    mostrar_fecha_inicio()

    print("\nAntes de ingresar al sistema debe validar la contraseña.")

    acceso_permitido = validar_contrasena()

    if not acceso_permitido:
        print("\nAcceso denegado. No puede ingresar al sistema.")
        return

    print("\nAcceso concedido. Bienvenido al sistema.")

    muestra_edades = None
    estadisticas = None

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == "1":
            muestra_edades = ingresar_muestra_edades()
            estadisticas = None

        elif opcion == "2":
            estadisticas = opcion_calcular_estadisticas(muestra_edades)

        elif opcion == "3":
            opcion_mostrar_reporte(muestra_edades, estadisticas)

        elif opcion == "4":
            print("\nGracias por utilizar el sistema.")
            print("Programa finalizado.")
            break


if __name__ == "__main__":
    iniciar_aplicacion()