import cv2
import numpy as np

# Inicializa la captura de la cámara. Puede variar según la cámara que estés utilizando.
cap = cv2.VideoCapture(0)

# Asegúrate de que la cámara se haya inicializado correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

# Leer la plantilla en escala de grises
template = cv2.imread("lempira.jpg", cv2.IMREAD_GRAYSCALE)

# Obtener las dimensiones de la plantilla
w, h = template.shape[::-1]

while True:
    # Capturar un cuadro de video desde la cámara
    ret, frame = cap.read()

    if not ret:
        print("Error al capturar el cuadro de video.")
        break

    # Convertir el cuadro de video a escala de grises
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Realizar la operación de coincidencia
    res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)

    # Establecer un umbral para detectar coincidencias
    threshold = 0.3

    # Encontrar las coordenadas de las coincidencias
    loc = np.where(res >= threshold)

    # Dibujar rectángulos alrededor de las coincidencias en el cuadro de video
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

    # Mostrar el cuadro de video con las coincidencias resaltadas
    cv2.imshow('Detected', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura de la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
