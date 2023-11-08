import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread("cat.jpg")

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización para separar el primer plano del fondo
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Invertir la máscara para que el primer plano sea blanco y el fondo sea negro
mask = cv2.bitwise_not(thresh)

# Crear una imagen con fondo transparente
result = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

# Aplicar la máscara al canal alfa para hacer el fondo transparente
result[:, :, 3] = mask

# Guardar la imagen resultante
cv2.imwrite("imagen_sin_fondo.png", result)

# Mostrar la imagen con el fondo eliminado
cv2.imshow("Imagen sin fondo", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
