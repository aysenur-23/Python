import cv2
import numpy as np

# resmi içeri aktar
image = cv2.imread("img3.jpg")

# resmi griye çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# kenar tespiti
edges = cv2.Canny(gray, 50, 150)


contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) > 0:
 
    drawing_contour = max(contours, key=cv2.contourArea)

    # Çizim konturunun etrafındaki sınırlayıcı dikdörtgeni hesapla
    x, y, w, h = cv2.boundingRect(drawing_contour)

    # Sınırlayıcı dikdörtgene dolgu ekleyin
    padding = 10  # Çizim ve çerçeve arasındaki mesafeyi değiştirmek için bu değeri ayarla
    x -= padding
    y -= padding
    w += 2 * padding
    h += 2 * padding

    # Çizimle aynı boyutta boş bir çerçeve oluştur
    frame = np.zeros_like(image)

    # Çerçeveyi dış kontur etrafında tek bir çizgi olarak çiz
    cv2.drawContours(frame, [drawing_contour], -1, (255, 0, 0), 1)

    # Çerçeveyi orijinal görüntünün üzerine yerleştirin
    result = cv2.addWeighted(image, 1, frame, 0.5, 0)

    # Sonucu görüntüle ve kaydet
    cv2.imshow("Result", result)
    cv2.imwrite("output.jpg", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No drawing detected in the image.")
