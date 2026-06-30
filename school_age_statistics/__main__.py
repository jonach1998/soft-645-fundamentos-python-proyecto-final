from datetime import datetime


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
    print("1. Ingresar edades y calcular estadísticas")
    print("2. Salir")


def leer_opcion():
    """
    Solicita una opción del menú y valida que sea correcta.
    """
    while True:
        opcion = input("Seleccione una opción: ").strip()

        if opcion in ["1", "2"]:
            return opcion

        print("Opción inválida. Debe seleccionar 1 o 2.")


def opcion_calcular_estadisticas():
    """
    Opción temporal mientras se desarrollan los demás módulos del proyecto.
    """
    print("\nEsta opción todavía está en desarrollo.")
    print("Cuando estén listas las demás clases, aquí se integrará:")
    print("- Validación de contraseña")
    print("- Solicitud del tamaño de la muestra")
    print("- Ingreso de edades")
    print("- Cálculo de estadísticas")
    print("- Reporte final")


def iniciar_aplicacion():
    """
    Función principal que controla el flujo del programa.
    """
    mostrar_fecha_inicio()

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == "1":
            opcion_calcular_estadisticas()

        elif opcion == "2":
            print("\nGracias por utilizar el sistema.")
            print("Programa finalizado.")
            break


if __name__ == "__main__":
    iniciar_aplicacion()