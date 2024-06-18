import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
from scipy.special import softmax

# Función de preprocesamiento
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

# Modelo y Tokenizer
MODEL = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

# Función para analizar el sentimiento
def analizar_sentimiento(text):
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    output = model(**encoded_input)
    scores = output.logits[0].detach().numpy()
    scores = softmax(scores)
    
    ranking = np.argsort(scores)[::-1]
    labels_scores = []
    for i in range(scores.shape[0]):
        label = config.id2label[ranking[i]]
        score = scores[ranking[i]]
        labels_scores.append(f"{label}: {np.round(float(score), 4)}")
    return "\n".join(labels_scores)

with open('Datasets/Transcripcion.txt', 'r', encoding='utf-8') as archivo:
    # Lee el contenido del archivo
    contenido = archivo.read()

resultado = analizar_sentimiento(contenido)
print(resultado)