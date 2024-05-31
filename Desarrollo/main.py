from transformers import pipeline
import pandas as pd

def Analizar(texto):
  # creación del pipeline cargando el modelo preentrenado
  pipe = pipeline(
      model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
      top_k=None)

  # obtención de la predicción
  evaluacion = pipe(texto)[0]

  # procesamiento de la respuesta del modelo
  if evaluacion[0]['label']=='negative': neg = evaluacion[0]['score']
  elif evaluacion[0]['label']=='positive': pos = evaluacion[0]['score']
  else: neu = evaluacion[0]['score']

  if evaluacion[1]['label']=='negative': neg = evaluacion[1]['score']
  elif evaluacion[1]['label']=='positive': pos = evaluacion[1]['score']
  else: neu = evaluacion[1]['score']

  if evaluacion[2]['label']=='negative': neg = evaluacion[2]['score']
  elif evaluacion[2]['label']=='positive': pos = evaluacion[2]['score']
  else: neu = evaluacion[2]['score']

  return (neg, neu, pos)

# Definir los límites de cada categoría
def clasificar_satisfaccion(negativo, neutro, positivo):
    if positivo >= 0.8:
        return "Muy satisfecho"
    elif positivo >= 0.6:
        return "Satisfecho"
    elif neutro >= 0.4:
        return "Neutral"
    elif negativo >= 0.6:
        return "Muy insatisfecho"
    elif negativo >= 0.4:
        return "Insatisfecho"
    else:
        return "Neutral"

# archivo con el dataset
archivo_csv = 'Datasets/texto_limpio.csv'
conversaciones = pd.read_csv(archivo_csv)

# resultados
resultados = []

for index, conversacion in conversaciones.iterrows():
    texto = conversacion['conversacion_cliente']
    neg, neu, pos = Analizar(texto)
    satisfaccion = clasificar_satisfaccion(neg, neu, pos)
    resultados.append([index, texto, satisfaccion])

df = pd.DataFrame(resultados, columns=['index', 'texto', 'clasificacion'])
# Nombre del archivo
archivo_csv = 'resultados.csv'
# Escribir el DataFrame en un archivo CSV
df.to_csv(archivo_csv, index=False)