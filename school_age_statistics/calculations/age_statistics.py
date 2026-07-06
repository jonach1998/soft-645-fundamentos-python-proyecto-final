def calculo_edad_máxima (muestra_edades):
  return max(muestra_edades["ages"])

def calculo_edad_minima (muestra_edades):
  return min(muestra_edades["ages"])

def calculo_promedio_edades (muestra_edades):
  edades = muestra_edades ["ages"]
  promedio = sum(edades)/ len(edades)
  return round(promedio, 1)

def calculo_mediana_edades (muestra_edades):
  edades = sorted (muestra_edades["ages"])

total = len(edades)
centro = total // 2

if total % 2 == 1:
  return edades[centro]

return (edades[centro -1] + edades [centro]) / 2

def calcular_estadisticas(muestra_edades): #Para respetar como esta hecho en Main.
  return {
    "edad_max": calculo_edad_máxima(muestra_edades),
    "edad_min": calculo_edad_minima(muestra_edades),
    "edad_promedio": calculo_promedio_edades(muestra_edades),
    "edad_mediana": calculo_mediana_edades(muestra_edades),}
  
