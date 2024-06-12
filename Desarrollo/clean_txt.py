# Define el nombre del archivo
nombre_del_archivo = 'Datasets/Transcript.txt'

# Nombre del cliente
nombre_cliente = 'Maylon Perez'

# Abre el archivo en modo de lectura
with open(nombre_del_archivo, 'r', encoding='utf-8') as archivo:
    # Lee todas las líneas del archivo
    lineas = archivo.readlines()

# Lista para almacenar las líneas del cliente
lineas_cliente = []

# Variable para indicar si estamos dentro de un diálogo del cliente
es_dialogo = False

# Itera sobre las líneas del archivo
for linea in lineas:
    if es_dialogo and linea != '\n':
        lineas_cliente.append(linea.strip())

    # Verifica si la línea actual es dicha por el cliente
    if linea.startswith(nombre_cliente):
        es_dialogo = True
    elif linea.startswith("\n"):
        es_dialogo = False


# Une las líneas del cliente en un solo texto
texto_cliente = "\n".join(lineas_cliente)


with open('Datasets/Transcripcion.txt', 'w', encoding='utf-8') as archivo:
    archivo.write(texto_cliente)