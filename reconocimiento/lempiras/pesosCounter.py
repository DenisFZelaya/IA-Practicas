import cv2
import numpy as np

imgPrincipal = "varios.jpg"
imgBuscar = "lempira.jpg"

# Leer la imagen principal en escala de grises
gray_img = cv2.imread(imgPrincipal, cv2.IMREAD_GRAYSCALE)

# Leer la plantilla en escala de grises
template = cv2.imread(imgBuscar, cv2.IMREAD_GRAYSCALE)

# Obtener las dimensiones de la plantilla
w, h = template.shape[::-1]

# Realizar la operación de coincidencia
res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)

# Establecer un umbral para detectar coincidencias
threshold = 0.3

# Encontrar las coordenadas de las coincidencias
loc = np.where(res >= threshold)

# Crear una copia de la imagen principal en color para dibujar rectángulos
img_rgb = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)

# Dibujar rectángulos alrededor de las coincidencias
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

# Mostrar la imagen con las coincidencias resaltadas
cv2.imshow('Detected', img_rgb)

# Esperar hasta que se presione una tecla y luego cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()
