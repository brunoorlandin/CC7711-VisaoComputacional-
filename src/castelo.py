import math
import numpy as np
import cv2
import matplotlib.pyplot as plt

#Importa e converta para RGB
img = cv2.imread('./img/castelo.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Convertendo para preto e branco (RGB -> Gray Scale -> BW)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
a = img_gray.max()

tamanhoKernel = 5
kernel = np.ones((tamanhoKernel,tamanhoKernel), np.uint8)

#Filtro de ruído (bluring)
img_blur = cv2.blur(img_gray, ksize=(tamanhoKernel,tamanhoKernel))

# Detecção borda com Canny (com blurry)
edges_blur = cv2.Canny(image=img_blur, threshold1=a/2, threshold2=a/2)

# Contorno
contours, hierarchy = cv2.findContours(
  image = edges_blur,
  mode = cv2.RETR_TREE,
  method = cv2.CHAIN_APPROX_SIMPLE
)
contours = sorted(contours, key = cv2.contourArea, reverse = True)
img_copy = img.copy()
finalImage = cv2.drawContours(
  img_copy, contours, 
  contourIdx = -1,
  color = (255, 0, 0), 
  thickness = 2
)

#plot imagens
imagens = [img,img_gray,img_blur,edges_blur,finalImage]
formatoX = math.ceil(len(imagens)**.5)
if (formatoX**2-len(imagens))>formatoX:
    formatoY = formatoX-1
else:
    formatoY = formatoX
for i in range(len(imagens)):
    plt.subplot(formatoY, formatoX, i + 1)
    plt.imshow(imagens[i],'gray')
    plt.xticks([]),plt.yticks([])
plt.show()

#plot imagens
imagens = [finalImage]
formatoX = math.ceil(len(imagens)**.5)
if (formatoX**2-len(imagens))>formatoX:
    formatoY = formatoX-1
else:
    formatoY = formatoX
for i in range(len(imagens)):
    plt.subplot(formatoY, formatoX, i + 1)
    plt.imshow(imagens[i],'gray')
    plt.xticks([]),plt.yticks([])
plt.show()
