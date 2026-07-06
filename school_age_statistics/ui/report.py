from datetime import datetime

def mostrar_reporte(muestra_edades, estadisticas):
    """
    Muestra el reporte final por consola.

  solo recibe los datos ya
    procesados por data_entry (muestra_edades) y calculations
    (estadisticas), y se encarga de presentarlos de forma clara.

    """
    if muestra_edades is None:
        print("\nPrimero debe ingresar una muestra de edades (opción 1).")
        return

    if estadisticas is None:
        print("\nPrimero debe calcular las estadísticas (opción 2).")
        return

    ahora = datetime.now()

    print("\n" + "=" * 45)
    print("REPORTE DE ESTADÍSTICAS DE EDADES")
    print("Colegio San Pascualin")
    print("=" * 45)
    print(f"Fecha: {ahora.strftime('%d/%m/%Y')}    Hora: {ahora.strftime('%H:%M:%S')}")
    print("-" * 45)
    print(f"Tamaño de la muestra: {muestra_edades['sample_size']}")
    print("Edades ingresadas:")

    for posicion, edad in enumerate(muestra_edades["ages"], start=1):
        print(f"  #{posicion}: {edad}")

    print("-" * 45)
    print(f"Edad mayor  : {estadisticas['max_age']}")
    print(f"Edad menor  : {estadisticas['min_age']}")
    print(f"Promedio    : {estadisticas['average']}")
    print(f"Mediana     : {estadisticas['median']}")
    print("=" * 45)