import pandas as pd 

# Especifica la ruta a tu archivo CSV
archivo_csv = 'Datasets/phone_calls.csv'

# Lee el archivo CSV en un DataFrame de pandas
conversations = pd.read_csv(archivo_csv)

conversaciones_filtradas = []

for index, conversation in conversations.iterrows():
    # Dividir el texto en líneas
    lineas = conversation['prompt'].split('\n')

    # Filtrar líneas que contienen 'Customer:'
    lineas_customer = [linea for linea in lineas if 'Customer:' in linea]

    # Unir las líneas filtradas en un texto
    resultado = '\n'.join(lineas_customer)
    resultado = resultado.replace('Customer:','')

    conversaciones_filtradas.append(resultado)

# Se guarda en un dataframe el resultado
df = pd.DataFrame(conversaciones_filtradas, columns=['conversacion_cliente'])

# Nombre del archivo
archivo_csv = 'Datasets/texto_limpio.csv'
# Escribir el DataFrame en un archivo CSV
df.to_csv(archivo_csv, index=False)