def mostrar_reporte(muestra_edades, estadisticas):
    """
    Retorna:
        True  si el reporte se mostró correctamente.
        False si faltaban datos (muestra_edades o estadisticas es None).
              En ese caso, quien llama a esta función decide qué mensaje
              mostrarle al usuario.
    """
    if muestra_edades is None or estadisticas is None:
        return False
 
    print("\n" + "=" * 45)
    print("REPORTE DE ESTADÍSTICAS DE EDADES")
    print("Colegio San Pascualin")
    print("=" * 45)
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
 
    return True