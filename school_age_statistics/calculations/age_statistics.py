def calcular_edad_maxima (muestra_edades):
  return max(muestra_edades["ages"])

def calcular_edad_minima (muestra_edades):
  return min(muestra_edades["ages"])

def calcular_promedio_edades (muestra_edades):
  edades = muestra_edades ["ages"]
  promedio = sum(edades)/ len(edades)
  return round(promedio, 1)

def calcular_mediana_edades(muestra_edades):
    edades = sorted(muestra_edades["ages"])

    total = len(edades)
    centro = total // 2

    if total % 2 == 1:
        return edades[centro]

    return (edades[centro - 1] + edades[centro]) / 2

def calcular_estadisticas(muestra_edades): #Para respetar como esta hecho en Main.
  return {
    "max_age": calcular_edad_maxima(muestra_edades), #Basandonos en Reportes
    "min_age": calcular_edad_minima(muestra_edades), #Basandonos en Reportes
    "average": calcular_promedio_edades(muestra_edades), #Basandonos en Reportes
    "median": calcular_mediana_edades(muestra_edades),} #Basandonos en Reportes
  
