import cv2
import numpy as np

def zoom_out_frame(image_path, zoom_level):
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not open or find the image.")
        return

    # Görüntüyü gri tonlamaya dönüştür
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Canny kenar algılamayı uygula
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Boşlukları birleştirmek için kenarları genişlet
    dilated = cv2.dilate(edges, None, iterations=2)

    # Find the contours of the shapes
    contours, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Şekillerin dış hatlarını bul
    for contour in contours:
        if len(contour) > 0:
            # Konturun merkezini hesapla
            moments = cv2.moments(contour)
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])

           # Uzaklaştırma için ölçek faktörünü hesapla
            scale_factor = 1 - zoom_level

            # Her noktayı ölçek faktörü kadar dışa doğru hareket ettir
            for point in contour:
                point[0][0] = int(cx + (point[0][0] - cx) * scale_factor)
                point[0][1] = int(cy + (point[0][1] - cy) * scale_factor)

            # Değiştirilen konturu çizin
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

    # Değiştirilen görüntüyü uzaklaştırılmış çerçeveyle kaydedin
    output_path = 'zoomed_out_image2.jpg'
    cv2.imwrite(output_path, image)

    print("Zoomed-out image saved successfully as zoomed_out_image.png")

image_path = "C:/Users/aslan/Downloads/img3.jpeg"
zoom_level = -0.2  #  (0.1 10% )
zoom_out_frame(image_path, zoom_level)
