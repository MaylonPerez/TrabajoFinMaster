# Define el nombre del archivo
nombre_del_archivo = 'Datasets/Transcript.txt'

# Nombre del cliente
nombre_cliente = 'Maylon Perez'

# Abre el archivo en modo de lectura
with open(nombre_del_archivo, 'r', encoding='utf-8') as archivo:
    # Lee todas las líneas del archivo
    lineas = archivo.read()

lineas = lineas.split('\n')

# Lista para almacenar las líneas del cliente
lineas_cliente = []

# Variable para indicar si estamos dentro de un diálogo del cliente
es_dialogo = False

# Itera sobre las líneas del archivo
for linea in lineas:
    if es_dialogo and linea != "":
        lineas_cliente.append(linea.strip())

    # Verifica si la línea actual es dicha por el cliente
    if linea.startswith(nombre_cliente):
        es_dialogo = True
    elif linea == '':
        es_dialogo = False


# Une las líneas del cliente en un solo texto
texto_cliente = "\n".join(lineas_cliente)


with open('Datasets/Transcripcion.txt', 'w', encoding='utf-8') as archivo:
    archivo.write(texto_cliente)

import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
from scipy.special import softmax

# Modelo y Tokenizer
MODEL = "j-hartmann/emotion-english-distilroberta-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

encoded_input = tokenizer(texto_cliente, return_tensors='pt', truncation=True, padding=True, max_length=512)

output = model(**encoded_input)
scores = output.logits[0].detach().numpy()
scores = softmax(scores)
ranking = np.argsort(scores)[::-1]
labels_scores = []
for i in range(scores.shape[0]):
    label = config.id2label[ranking[i]]
    score = scores[ranking[i]]  
    labels_scores.append(f"{label}: {np.round(float(score), 4)}")
    res = " ".join(labels_scores)

print(res)